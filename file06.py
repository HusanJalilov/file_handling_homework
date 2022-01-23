def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x=data.split()
    a=[]
    idx=0
    while idx < len(x):
        print(data[idx])
        a.append(len(x[idx]))
        idx+1
    return a

    

    
# Read data from file