from typing import List

def measure_if_greater(list_of_depth:List,window:int=3)->int:
    depth_increase_counter=0
    prev_sum=0
    for depth_index in range(3,len(list_of_depth)):
        curr_sum = list_of_depth[depth_index-2]+list_of_depth[depth_index-1]+list_of_depth[depth_index]
        if curr_sum>prev_sum:
            depth_increase_counter=depth_increase_counter+1
        prev_sum=curr_sum
    return depth_increase_counter
