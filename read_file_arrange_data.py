import sys
import argparse

class Process:
    def __init__(self,file_path, keyword='PID'):
        self.file_path = file_path
        self.keyword = keyword
        self.col_names = []
    def load_file_data(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                yield line.rstrip('\n')
    def process_data(self):
        start = 1
        line_num = 1
        header=None
        process = []
        found_pid=False
        for line in self.load_file_data():
            if 'PID' in line and not found_pid:
                start=line_num
                header = line.split()
                ncols = len(header)
                found_pid=True
            if line_num>start and found_pid:
                tem_dict={}
                row = line.split()
                command_value = ' '
                tail_end = []
                for i, value in enumerate(row):
                    if i<ncols-1:
                        tem_dict[header[i]] =value
                        
                    else:
                        tail_end.append(value)
                comm=command_value.join(tail_end)
                tem_dict[header[ncols-1]] = comm
                process.append(tem_dict)
                
            line_num+=1
        return process
            
if __name__=='__main__':
    parser = argparse.ArgumentParser(description="read file")
    parser.add_argument("file_name", help="provide file name")
    args = parser.parse_args(sys.argv[1:])
    filename = args.file_name
    process =Process(filename)
    print(process.process_data(),"\n")

 

# count= count+1 
#     print(begins_at)