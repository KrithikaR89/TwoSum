import logging
import sys

class Solution(object):
    def __init__(self):
        logging.getLogger().setLevel(logging.INFO)
        logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %I:%M:%S')
        print('\n')
        logging.info("****************** Two sum problem ****************")
        
    def inputs(self):
        """
        param: None
        return: input_list : List for processing
        return: input_number : Number to target for summation
        """
        input_number = None
        logging.info("Please enter numbers separated by spaces")
        input_list = (sys.stdin.readline().strip()).split( )
        logging.info("Please enter 1 target number")
        number = sys.stdin.readline().strip()
        
        try:
            input_number = int(number)
            if isinstance(input_list,list):
                for i, v in enumerate(input_list):
                    input_list[i] = int(v)
        except ValueError:
            logging.error("Aborting run - Invalid input list or target number provided")
            logging.info("Please provide a list with numbers only")
            logging.info("Please provide a a target number that is an integer only")
            return None, None

        if input_number < 0 and all(x<0 for x in input_list):
            logging.info("Special case number & list conversion since both are negative")
            input_number = abs(input_number)
            input_list = list(abs(x) for x in input_list)

        return input_list,input_number
    
    def twoSum(self, input_list, input_number):
        """
        param: List for processing, Number to target for summation
        return: List of indices whose elements sum to the target 
        """
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
    if input_list and input_number or input_number==0:
        accepted_indices = ts.twoSum(input_list, input_number)
        if accepted_indices:
            for indice in accepted_indices:
                logging.info("Here are the indices in your list that add up to your target: {0!s}"
                    .format(indice))
