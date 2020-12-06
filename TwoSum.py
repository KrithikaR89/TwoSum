import logging
#import input

class Solution(object):
    logging.info("Two sum problem")
    
    def __init__(self):
        logging.getLogger().setLevel(logging.INFO)
        logging.basicConfig(format='%(levelname)s:%(message)s')
        
    def inputs(self):
        input_number = None
        #input_list = input("Please enter list of numbers")
        #number = input("Please enter target number")
        input_list = [0,3,4,0]
        number = 0
        
        if isinstance(number,int) or number.isdigit():
            if isinstance(input_list,list):
                logging.info("Format valid for input list & target number")
                input_number = int(number)
            
            for i,v in enumerate(input_list):
                if isinstance(v,int):
                    pass    
                elif v.isdigit():
                    logging.info("Converting string element in list to int")
                    input_list[i] = int(v)
                else:
                    logging.error("Aborting run - Invalid list provided")
                    return None, None
            
            if input_number < 0 and all(x<0 for x in input_list):
                logging.info("Special case number & list conversion since both are negative")
                input_number = abs(input_number)
                for i,v in enumerate(input_list):
                    input_list[i] = abs(v) 
            return input_list,input_number
        
        logging.error("Aborting run - Invalid input list or target number provided")
        return None, None
    
    def twoSum(self, input_list, input_number):
        logging.info("Calculating indices for target number")
        rejected_indices = []
        accepted_indices = []

        if input_number==0 and any(x<0 for x in input_list):
            for i, v in enumerate(input_list):
                if v < 0:
                    for position in range(len(input_list)-1):
                        adder = len(input_list)-(position+1)
                        if abs(v) == input_list[adder]:
                            accepted_indices.append([i, adder])
            return accepted_indices

        else:
            if all(x>0 for x in input_list):
                for i,v in enumerate(input_list):
                    if v >= input_number:
                        rejected_indices.append(i)
                
            logging.info("Following indices have been rejected as being larger than target : {0!s}"
                        .format(rejected_indices))
                    
            for i,v in enumerate(input_list):
                for position in range(len(input_list)-1):
                    adder = len(input_list)-(position+1)
                    if i not in rejected_indices and adder not in rejected_indices and i != adder:
                        if input_list[adder]+v == input_number:
                            accepted_indices.append([i, adder])
                    else:
                        pass
                
        return accepted_indices

if __name__ == '__main__':    
    ts = Solution()
    input_list, input_number = ts.inputs()
    print(input_list)
    print(input_number)
    if input_list and input_number or input_number==0:
        accepted_indices = ts.twoSum(input_list, input_number)
        for indice in accepted_indices:
            logging.info("Here are the indices in your list that add up to your target: {0!s}"
                    .format(indice))
