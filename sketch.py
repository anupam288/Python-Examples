import os

os.getcwd()
os.chdir('C:\\Users\\abansal\\Documents\\Python Libraries')
man = []
other = []

with open('sketch.txt') as data:    
    try:
        for each_line in data:
            try:
                      
                if(not each_line.find(':') == -1):
                    (role,line_spoken) = each_line.split(':',1)

                    line_spoken = line_spoken.strip()

                    if(role == 'Man'):
                        man.append(line_spoken)
                    elif(role == 'Other Man'):
                        other.append(line_spoken)
                        
                    print(role,end='')
                    print(' said = ',end = '')
                    print (line_spoken)
                else:
                    print(each_line,end='')
                    
            except ValueError:

                pass
                
    except IOError:
        print('File does not exist')


try:

    with open('man_data.txt','w') as man_file , open('other_man_data.txt','w') as other_file:
        print(man,file = man_file)
        print(other,file = other_file)

except IOError:
    print('File Error')

