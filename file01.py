def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list1 = data.split(',')
    list1 = list(map(int,list1))
    return list1
