# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Brian F. Thomas

import numpy

class DynamicArray(object):

    def __init__(self):
        self.capacity = 10  # Capacity of array
        self.arrayContent = numpy.ndarray(self.capacity, 'O')  # Array to hold input objects
        self.next_index = 0  # Current array index
        self.data = numpy.ndarray(self.capacity, 'O')

    def __len__(self):
        """
        Returns the amount of elements in the array
        """
        return self.next_index

    def __getitem__(self, index):
        """
        Allow subscripting of the Dynamic Array
        """
        # return self.arrayContent[index]
        if self.next_index > index >= 0:
            return self.arrayContent[index]  # Return requested index value
        else:
            raise IndexError

    def is_empty(self):
        """
        Return whether or not the array is empty
        """
        # Check if on 0 index
        if self.next_index == 0:
            return True
        else:
            return False

    def is_full(self):
        """
        Checks if the array is at capacity
        """
        if self.next_index < self.capacity:
            return False
        else:
            return True

    def __increase_capacity(self):
        """
        Doubles the array capacity when called
        """
        self.capacity *= 2  # Increase array capacity
        self.arrayContent = numpy.ndarray(self.capacity, 'O')  # Create expanded array
        for i in range(0, len(self.data)):  # Write existing data into expanded array
            self.arrayContent[i] = self.data[i]
        self.data = self.arrayContent.copy()  # Synchronize data and array content

    def append(self, val):
        """
        Add a new element to the end of the array
        """
        if not self.is_full():
            self.arrayContent[self.next_index] = val  # Add value to the array
            self.data[self.next_index] = val  # Add value to internal data storage
            self.next_index += 1  # Advance the index
        else:
            self.__increase_capacity()  # Expand the array
            self.append(val)

    def clear(self):
        """
        Removes all elements from the array and resets to initial state
        """
        self.__init__()  # Call the init method to reset the array

    def pop(self):
        """
        Remove the last element in the array
        """
        if self.next_index > 0:  # Verify array is not empty
            self.next_index -= 1  # Decrement index
            temp = self.arrayContent[self.next_index]  # Create temp for the return value
            self.arrayContent[self.next_index] = None  # Clear the last element
            return temp
        else:
            raise IndexError

    def delete(self, index):
        """
        Removes the element at selected index
        """
        if 0 <= index < self.next_index:  # Check if in range
            for i in range(index, self.next_index):
                self.arrayContent[i] = self.arrayContent[i+1]  # Move data to the left
            self.data = self.arrayContent.copy()  # Synchronize array and data objects
            self.next_index -= 1  # Decrease index counter
        else:
            raise IndexError

    def insert(self, index, val):
        """
        Inserts a value at the given index
        """
        if not self.is_full():
            if 0 <= index <= self.next_index:  # Check if in range
                for i in range(index, self.next_index):  # Move current data to the right
                    self.arrayContent[i + 1] = self.data[i]
                self.arrayContent[index] = val  # Insert the new value
                self.data = self.arrayContent.copy()  # Synchronize array and data objects
                self.next_index += 1  # Advance index counter
            else:
                raise IndexError
        else:
            self.__increase_capacity()
            self.insert(index, val)

    def max(self):
        """
        Return the largest value in the array
        """
        max_val = self.arrayContent[0]  # Set max to first object in array
        for i in range(0, self.next_index):  # Check each value
            if self.arrayContent[i] > max_val:
                max_val = self.arrayContent[i]  # If value is larger than current max, update current max
        return max_val

    def min(self):
        """
        Return the smallest value in the array
        """
        min_val = self.arrayContent[0]  # Set min to first object in array
        for i in range(0, self.next_index): # Check each value
            if self.arrayContent[i] < min_val:
                min_val = self.arrayContent[i]  # If value is smaller than current min, update current min
        return min_val

    def sum(self):
        """
        Return the sum of all values in the array
        """
        array_sum = self.arrayContent[0]
        for i in range(0, self.next_index):
            array_sum += self.arrayContent[0]
        return array_sum

    def linear_search(self, val):
        """
        Performs a linear search for a value in the array
        """
        for i in range(0, self.next_index):
            if self.arrayContent[i] == val:
                return i
        return None

    def binary_search(self, val):
        """
        Recursive helper method
        """
        left = 0
        right = self.next_index - 1
        return self.__rec_binary_search(val, left, right)

    def __rec_binary_search(self, val, left, right):
        """
        Performs a recursive binary search for value input into helper method and returns the index of the value or None
        """
        if left <= right:
            mid = (left + right) // 2
            if self.arrayContent[mid] == val:  # If target value has been found, return index
                return mid
            elif self.arrayContent[mid] < val:  # If current index is smaller than target, call recursion
                return self.__rec_binary_search(val, mid + 1, right)
            else:  # If current index is larger than target, call recursion
                return self.__rec_binary_search(val, left, mid - 1)
        else:
            return None