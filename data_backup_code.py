#Importing libraries
from datetime import date, datetime
import os
from calendar import monthrange, day_name

#Creating a Databackup class
class DataBackup():
    def __init__(self, curr_date, f_date):
        self.curr_date = curr_date
        self.f_date = f_date

    def check_last_Fivedays(self, f_name):
        """
        Checks if the file is older than 5 days

        :param f_name: name of file
        :return: true for files older than five days else false
        """
        day_diff = self.curr_date - self.f_date
        if day_diff.days >= 5:
            return True
        else:
            return False



    def check_Sat(self, f_name):
        """
        Checks if the file is from a saturday
        
        :param f_name: name of file
        :return: true for files with date of Saturday else false
        """
        if day_name[self.f_date.weekday()] == 'Saturday':
                return True
        else:
            return False



    def check_last_Day_of_Month(self, f_name):
        """
        Checks if the file is from last day of month
        
        :param f_name: name of file
        :return: true for files having date of last day of month else false
        """
        if self.f_date.day == monthrange(self.f_date.year, self.f_date.month)[1]:
            return True
        else:
            return False

if __name__ == "__main__":
    #current_date = datetime.now()
    
    current_date = datetime.strptime('2020-9-18', '%Y-%m-%d')   #Taking a date as current date
    
                                                                
    print("Enter bucket name like bucket1 bucket2 (space seperated)")                          
    bucket = [x for x in input().split()]

    for i in range(len(bucket)):
        sat_file_count_for_bucket = 0
        print('Iterating through  ' +bucket[i] +' directory...\n')
        print("Deleting following files in " +bucket[i]+" : \n")
        
        for entry in os.listdir(bucket[i]+'/'):
            start = entry.rfind('_') + 1
            end = entry.find('.')
            f_date = entry[start:end]

            #datetime of file
            file_date = datetime.strptime(f_date, '%Y-%m-%d')
            a = DataBackup(current_date, file_date)
            if a.check_last_Fivedays(entry):
                if a.check_Sat(entry) == False:
                    if a.check_last_Day_of_Month(entry) == False:
                        print(entry)
                        os.remove(bucket[i]+'/'+entry)
                else:
                    if sat_file_count_for_bucket > 4:
                        if a.check_last_Day_of_Month(entry) == False:
                            print(entry)
                            os.remove(bucket[i]+'/'+entry)
                    else:
                        sat_file_count_for_bucket += 1

    

#printing remaining files in buckets
for i in range(len(bucket)):
    print("\nRemaining files in "+bucket[i]+" : \n")
    print('\n'.join(os.listdir(path=bucket[i]+'/')))
