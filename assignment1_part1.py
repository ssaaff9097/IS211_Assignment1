
def list_divide(numbers, divide=2):
    if divide == 0:
        raise ListDivideException()
    return sum(1 for number in numbers if number % divide ==0)
class ListDivideException(Exception):
    pass
   
    pass

def test_list_divide():
    assert list_divide([1,2,3,4,5]) == 2
    assert list_divide([2,4,6,8,10]) == 5
    assert list_divide([30, 54, 63,98, 100], divide=10) == 2
    assert list_divide([]) == 0
    assert list_divide([1,2,3,4,5], 1) == 5
    print("All tests passed!")
    
print("A test failed.")
    
if __name__ == "__main__":
    test_list_divide()
