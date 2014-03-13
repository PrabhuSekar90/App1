#!C:\python25\python.exe
class _test1(object):
    def list_data(self, file_path):
        data_list=None 
        try:
            file_obj = open(file_path,'r')
            try:
                gen = (line.split(',') for line in file_obj)  #here we split up each line to end of line in the file
                for j,line in enumerate(gen):
                    if not data_list:
                        data_list = [[] for i in range(len(line))]
                        if line[-1].find('\n'):
                            line[-1] = line[-1][:-1] 
                    for i,l in enumerate(line):
                        if i >=2 and j >= 1:
                            data_list[i].append(float(l))
                        else:            
                            data_list[i].append(l)
            except IOError, io_except:
                print io_except
            finally:
                file_obj.close()
        except IOError, io_exception:
            print io_exception

        return data_list

    def result_data(self, file_path):
        data_list = self.list_data(file_path)
        re=[]  
        if data_list:
            for i,d in enumerate(data_list):
                if i >= 2:
                    maxVal = max(data_list[i][1:])      
                    indedx = data_list[i].index(maxVal)   
                    yr = data_list[0][indedx]         
                    mon = data_list[1][indedx]        
                    com = data_list[i][0]          
                    re.append((maxVal,yr,mon,com))
            return re


if __name__ == '__main__':
    file_path = 'C:/Users/SNTAdmin/Desktop/test.csv'
   # value = result_data(file_path)
    print _test1().result_data(file_path)
    #print value
