"""
Author: Siew Ming Shern
StudentID: 28098552
"""
#------------------User Input -----------------------
def askUserAnswer(command,array):
    """
    :param command: string represent question to be ask to user
    :param array: list of words
    :return: nothing
    Time Complexity:
      Best Case: O(1), happens when user gives other value which is not "y", no need to print item in array
      Worst Case: O(n), Happens when user gives "y" and needs to print every item in array
      where n is number of words in array
    Space complexity:
      Best Case: O(1)
      Worst Case: O(1)
      Best Case == Worst Case, operation just involve getting item and print it.
    """
    uInput = input(command)
    if uInput.lower() == "y":
        for item in array:
            print(item)

def askUserAnswerK(command,array):
    """
    :param command: string represent question to be ask to user
    :param array: list of words
    :return: nothing
    Time Complexity:
      Best Case: O(n)
      Worst Case: O(n)
      where n is number of words in array
      Best Case == Worst Case, n times is needed to print every item of array, and cannot terminate early.
    Space complexity:
      Best Case: O(n)
      Worst Case: O(n)
      where n is number of words in array
      Best Case == Worst Case, list of array with n words is need for memory space.
    Error handling: ValueError occurs when k is given with character or floating number.
    """
    uInput = input(command)
    try:
        if '.' in uInput: raise ValueError("kth Number is accepted only")
        uInput = int(uInput)
    except ValueError:
        raise ValueError("kth Number is accepted only")
    newlist = kTopWords(uInput,array)
    print(str(uInput)+" top most words appear in the writing are: ")
    printWordAndCount(newlist)

def printWordAndCount(array):
    """
    :param command: string represent question to be ask to user
    :param array: list of words with counts
    :return: nothing
    Time Complexity:
      Best Case: O(n)
      Worst Case: O(n)
      where n is number of words in array
      Best Case == Worst Case, n times is needed to print every item of array, and cannot terminate early.
    Space complexity:
      Best Case: O(1)
      Worst Case: O(1)
      Best Case == Worst Case, operation just involve getting item and print it.
    """
    for item,count in array:
        print(item + " : " + str(count))

#------------------ Assignment -----------------------
#Task 1
def preprocess(filename):
    """
    :param filename: name of file
    :return: newArray, an array which consist of list of words without auxiliary verbs, articles and punctuation.
             empty Array, indirectly telling programs that file given does not have sufficient resources
             to continue the programs
    Time Complexity:
       Best Case: O(nm)
       Worst Case: O(nm)
       where n is number of words and m is maximum number of characters in a word.
       Best Case == Worst Case, File is open and read from character to character and will not be able to terminate early.
    Space complexity:
       Best Case: O(nm)
       Worst Case: O(nm)
       where n is number of words and m is maximum number of characters in a word.
       Best Case == Worst Case, List is created in memory requires to stores string representing n words with m characters,
       there is no way to save up memory space to store these words.
    """
    #tuple of auxiliary verbs and articles to be removed from words.
    exclusionStr = ('am', 'is', 'are','was', 'were', 'has', 'have', 'had', 'been', 'will', 'shall', 'may', 'can', 'would', 'should', 'might','could','a','an','the')

    #open and read file
    try:
        files = open(filename,"r")
        filecontent = files.read()
        files.close()
    #return empty array for indicating nothing to continue beyond here
    except FileNotFoundError:
        return []
    # when file content is empty, return empty array for indicating nothing to continue beyond here
    if len(filecontent) < 1: return []

    #variable that holds words which contain character that is accepted.
    currentString = ""

    newArray = []

    #iterate each character in file content
    for eachChar in range(len(filecontent)):
        #if current character is whitespace,
        #   check if currentstring that have been readed if it is article or auxilary verb
        #       true: skip and then reset currentstring
        #       false: append the string to list because it is valid words
        if ord(filecontent[eachChar]) == 10 or ord(filecontent[eachChar]) == 9 or ord(filecontent[eachChar]) == 32:
            if len(currentString) < 1 or currentString in exclusionStr :
                pass
            else:
                newArray.append(currentString)
            currentString = ""
        # any other character that is not white space or alphabet is ignore
        elif ord(filecontent[eachChar]) < 97 or ord(filecontent[eachChar]) > 122:
            pass
        #when character is valid, it can be accepted, therefore append with current string.
        else:
            currentString += filecontent[eachChar]
        #if current character is already last character of file and the length of current string is not empty
        #   check if the string is valid to be inserted to our list
        if eachChar == len(filecontent)-1 and len(currentString) > 0:
            if currentString in exclusionStr:
                pass
            else:
                newArray.append(currentString)
    #when length of array is empty indicates that not enough words to continue,
    #return empty array for indicating nothing to continue beyond here
    if len(newArray) < 1: return []

    return newArray

#Task 2
def wordSort(array):
    """
    This function act as radix sort.
    :param array: list of words
    :return:array: list of sorted words
    Time Complexity:
       Best Case: O(nm)
       Worst Case: O(nm)
       where n is number of words and m is maximum number of characters in a word.
       Best Case == Worst Case, Both cases would requires programs to Go through each word,
       looking at from far right character and, sort it and the words into the temporary array(created in counting sort).
       Since we have n words, it is O(n) for going through every words inclusive with replacing original list with item counting sort list.
       Then each n words has atmost m characters for the longest word in n words and we only need to consider 26 character at most in counting sort array,
       which will takes O(m). so we repeat m times giving us O(m) * O(n), resulting O(nm).
    Space complexity:
       Best Case: O(nm)
       Worst Case: O(nm)
       where n is number of words and m is maximum number of characters in a word.
       Best Case == Worst Case, input varies from n number of words with m maximum characters, input array will have n words with atmost m characters
       which would be taken as consideration for space complexity and Building array of size 27 to represent each for blank character and a-z character
       for counting sort array. therefore, constant size array is build and  the constant build array will need to store n words with
       atmost m characters in memory. This resulting O(nm).
    Error handling: No Error Exceptions.
    """
    # when array is empty return empty array
    if len(array) < 1 : return []
    # assumes maximumLength holds length of first string
    maximumLength = len(array[0])
    #iterate rest of item 1..N words, check for the maximum length of words
    for item in range(1, len(array)):
        if len(array[item]) > maximumLength:
            maximumLength = len(array[item])
    #at each iteration the position of words from last to first index of string,
    #perform countingsort array based on index of largest words uptill index 0.
    for position in range(maximumLength, 0, -1):
        countingSort(array, position)

    return array

def countingSort(array,position):
    """
    :param array: list of words.
    :param position: holds the position of current character 1..m, m is maximum character in n words.
    :return: nothing
    Time Complexity:
       Best Case: O(n)
       Worst Case: O(n)
       where n is number of words
       Best Case == Worst Case, counting sort always tranverse array with n words,
       Building array of size 27 to represent each for blank chracter and a-z character for counting sort array.
       therefore, constant size array is build. Then, looping through array for n times and insert each words to count array,
       and rebuild the original list from count array will takes O(n + n), resulting O(n).
    Space complexity:
       Best Case: O(nm)
       Worst Case: O(nm)
       where n is number of words and m is maximum number of characters in a word.
       Best Case == Worst Case, input varies from n number of words with m maximum characters, input array will have n words with atmost m characters
       which would be taken as consideration for space complexity and Building array of size 27 to represent each for blank character and a-z character
       for counting sort array. therefore, constant size array is build and  the constant build array will need to
       store n words with atmost m characters in memory. This resulting O(nm).
    Error handling: No Error Exceptions.
    """
    #create an array of ascii code from a-z(26) and a empty character(1)(for shorter length)
    newarray = [[] for i in range(27)]

    #store item in array based on thier ascii code
    for item in array:
        if len(item) < position:
            newarray[0].append(item)
        else:
            newarray[(ord(item[position-1])-97)+1] .append(item)

    #remove all item in array for new array.
    while len(array) > 0:
        array.pop()

    #copy all value from newarray back to original array
    for eachitem in newarray:
        if len (eachitem) > 0:
            for item in eachitem:
                array.append(item)

#Task 3
def wordCount(array):
    """
    :param array: sorted list of words
    :return: newarray: list with two valaue:
                       the total number of words and
                       a list of words with their count
    Time Complexity:
        Best Case: O(n)
        Worst Case: O(nm)
        where n is number of words and m is maximum character in words.
        Best Case: When every words have different length, it doesn't need to tranverse m times to compare two strings.
        Worst Case: when every words have same length, it would need to tranverse m times to compare each n words Making it O(n)*O(m) to O(nm).

    Space Complexity:
        Best Case: O(nm)
        Worst Case: O(nm)
        where n is number of words and m is maximum character in words.
        Best Case == Worst Case, this function will need to store n words with atmost m characters with thier count to list.
        so, it takes O(nm) to store n words and atmost m character and there is no way to save up memory space complexity.

    Error handling: No Error Exceptions.
    """
    #when array is empty return empty array
    if len(array) < 1: return []
    newarray = []
    #add total valid words(duplication is allowed) in original list.
    newarray.append(len(array))
    #let current words be first item
    currentword = array[0]
    wordnumber = 1
    #loops through array[1..N], starting from second item to last
    for item in range(1,len(array)):
        #when length(item) is not equal to current words,
        #we knows both words are not same,
        #therefore, add the currentword and count to new array
        #set currentword to currentitem of array
        if len(array[item]) != len(currentword):
            newarray.append([currentword, wordnumber])
            currentword = array[item]
            wordnumber = 1
        #when length of item is equal to currentword
        else:
            #when item in array is equal to currentword, increase count
            if array[item] == currentword:
                wordnumber += 1
            #when is not same words, add the currentword and count to new array
            #set currentword to currentitem of array
            else:
                newarray.append([currentword,wordnumber])
                currentword = array[item]
                wordnumber = 1
    #deals with invariant that previous loops could not do
    #last element are always checked but not added in to new array
    newarray.append([currentword,wordnumber])
    return newarray

#   Task 4
#   Actual codes for class is extracted from FIT1008, my_heap.py on week 12
#   https://lms.monash.edu/course/view.php?id=42395&section=19#19
class MinHeap:

    def __init__(self, count):
        """
        :param count: number of item to be inserted to this heap
        Time Complexity:
            Best Case:  O(k)
            Worst Case: O(k)
            where k is kth value specify by user.
            Best Case == Worst Case, this function will always create a list for N item .
        Space Complexity:
            Best Case:  O(k)
            Worst Case: O(k)
            where N is Maximum number of item that can be inserted to this class.
            Best Case == Worst Case, this function will always create a list for N item which require 4 bytes each N items.
        """
        self.count = 0
        self.array = [None] * (count+1)

    def __len__(self):
        """
        :return: self.count
        Time Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
            Best Case == Worst Case, this function is returning only number of item in This Heap excluding the first element,
            so that computation can be convienience.
        Space Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
            Best Case == Worst Case, this function will always return a byte for any number.
        """
        return self.count

    def swap(self, i, j):
        """
        :param i: index of an item in array
        :param j: index of an item in array
        :return: no return, it is void method.
        Time Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
            Best Case == Worst Case, this function is swapping position of two item in array.
        Space Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
            Best Case == Worst Case, no memory required for this operation since it does not create any memory for swapping.
        """
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def rise(self, k):
        """
        :param k: index of an item, mainly which is index of new item added to heap.
        :return: nothing to return, it is just swapping method for new item to fit in this heap.
        Time Complexity:
            Best Case:  O(1)
            Worst Case: O(log k)
            where k is number of non-empty item in list.

            Best Case: this function can terminate early if new child nodes is already bigger than parent nodes
            and if new child nodes is equal to parent nodes but already have bigger index value that it holds.
            Therefore, no swapping is required at all.
            Worst Case: when new child nodes is the smallest item of the heaps or the new child nodes is equal to all parent nodes
            but have a bigger index. Therfore, any time the new child nodes encounter any above cases, swapping is reuired at log n times
        Space Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
            Best Case == Worst Case, no memory required for this operation since it does not create any memory for swapping.
        """
        #rise item to parent nodes if parents is already bigger than current new nodes
        while k > 1 and self.array[self.getparent(k)][1] > self.array[k][1]:
            self.swap(k, self.getparent(k))
            k = self.getparent(k)
        # swapping parent with new nodes when it equals but have higher index value.
        while k > 1 and self.array[self.getparent(k)][1] == self.array[k][1] and self.array[self.getparent(k)][0] < self.array[k][0]:
            self.swap(k, self.getparent(k))
            k = self.getparent(k)

    def add(self, wordFreq, counter):
        """
        :param wordFreq: a value defines word count to be inserted in to array
        :param counter: index of that item in original list
        :return: nothing, just a void method
        Time Complexity:
            Best Case:  O(1)
            Worst Case: O(log k)
            where k is number of non-empty item in list.
            Best Case: this function can terminate early if new child nodes is already bigger than parent nodes
                and if new child nodes is equal to parent nodes but already have bigger index value that it holds.
                Therefore, no swapping is required at all.
            Worst Case: when new child nodes is the smallest item of the heaps or the new child nodes is equal to all parent nodes
                but have a bigger index. Therfore, any time the new child nodes encounter any above cases, swapping is reuired at log n times
        Space Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
            Best Case == Worst Case, no memory required for this operation since it does not create any memory for swapping.
        """
        newitem = [counter, wordFreq]
        #add item when current class length is less than heap array length
        if self.count + 1 < len(self.array):
            self.array[self.count + 1] = newitem
            self.count += 1
            self.rise(self.count)

    def getmin(self):
        """
        :return: get minimum value of frequency of an array which always located at index 1.
        Time Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
        Best Case == Worst Case, access item of array which only tooks O(1).
        Space Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
        Best Case == Worst Case, access item of array which only tooks O(1). Therefore, a byte memory is all its needs.
        """
        return self.array[1][1]

    def extract(self):
        """
        :return:
        Time Complexity:
            Best Case:  O(log k)
            Worst Case: O(log k)
            where k is number of non-empty item in list.
            BestCase == Worst Case: Happens when new roots node is needed to swap all the way to other item to become a leaf node.
        Space Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
        Best Case == Worst Case, This operation is just swapping operation(in-place function). Therefore, no memory is required to
        perform it.
        """
        #store item to new variable, swap last child nodes with root then reduce length of array
        item = self.array[1]
        self.swap(1, self.count)
        self.count -= 1
        #sink method is called to adjust array to heap structure.
        self.sink(1)
        return item

    def sink(self, k):
        """
        :param k: index of an item in array
        :return: nothing, just a void method
        Time Complexity:
            Best Case:  O(log k)
            Worst Case: O(log k)
            where k is number of non-empty item in list.
            When last item is swapped with root, it always require comparing with child node and needs to sink all the way to become leaf node
            because in heap structure, child node in scallability is always bigger than any parent nodes of older root node
        Space Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
        Best Case == Worst Case, This operation is just swapping operation(in-place function) therefore, no memory is required to
        perform it.
        """
        #if array has left item, loops continute
        while self.getleft(k) <= self.count:
            child = self.getsmallestchild(k)
            #when parent nodes is already smaller than child node, break
            if self.array[k][1] < self.array[child][1]:
                break
            #when parent nodes is already equal to child node, then index value with higher is place at root
            elif self.array[k][1] == self.array[child][1] and self.array[k][0] > self.array[child][0]:
                break
            self.swap(child, k)
            k = child

    def getparent(self,k):
        """
        :param k: refers to index of item in array
        :return: computation of parent of k index in array.
        Time Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
        Best Case == Worst Case, this function just performing arithmetic operation.
        Space Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
        Best Case == Worst Case, for this function just performing arithmetic operation. Therefore, a byte memory is all its needs
        """
        return k//2

    def getleft(self,k):
        """
        :param k: refers to index of item in array
        :return: computation to get left child nodes
        Time Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
        Best Case == Worst Case, this function just performing arithmetic operation.
        Space Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
        Best Case == Worst Case, for this function just performing arithmetic operation. Therefore, a byte memory is all its needs
        """
        return 2*k

    def getright(self,k):
        """
        :param k: refers to index of item in array
        :return: computation to get right child nodes
        Time Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
        Best Case == Worst Case, this function just performing arithmetic operation.
        Space Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
        Best Case == Worst Case, for this function just performing arithmetic operation. Therefore, a byte memory is all its needs
        """
        return 2*k + 1

    def getsmallestchild(self, k):
        """
        :param k: index of item in array
        :return: either left index of k item or right item of k index
        Time Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
            Best Case == Worst Case, this function just comparing which child nodes is smaller when last nodes is swap with minimum
            after extract() method is called.
        Space Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
            Best Case == Worst Case, This function only involve storing index into variable and accessing item in array.
            Therefore, two byte memory is all its needs resulting O(1)
        """
        left = self.getleft(k)
        right = self.getright(k)
        #check if there is length of class is equal to root with left item only or if left child is smaller, return left if true
        if left == len(self) or self.array[left][1] < self.array[right][1]:
            return left
        #check if there left child node is equal to right node and index value of left is bigger, return left if true
        elif self.array[left][1] == self.array[right][1] and self.array[left][0] > self.array[right][0]:
            return left
        #return right when we knew right node is assume smaller.
        else:
            return right

    def setReverse(self):
        """
        :return: self, which references to object created by this class.
        Time Complexity:
            Best Case:  O(k log k)
            Worst Case: O(k log k)
            where k is number of non-empty item in list.
            Best Case == Worst Case: Happens when at each k iteration, new parent nodes from last element that has been swap with
            root nodes is needed to sink() all the way to leaf nodes since it was originally a leaf node, and in heap, last item
            is always the biggest item of the rest item in min heap. Early termination is unlikely unless the height of heap is
            1 or 2, where input are too small to take accountable.
        Space Complexity:
            Best Case:  O(1)
            Worst Case: O(1)
            Best Case == Worst Case, This function only involve swapping item from root to last element at each k iteration
            where memory is not consumed and it is in-place function.
        """
        #store the original object length.
        originalLength = self.count
        #for each item in this class, extract minimum to make this heap array sorted in Descending order
        for item in range(len(self)):
            self.extract()
        #reinitialise the length back to self.count for iterator later.
        self.count = originalLength
        #return instance object for iterator purpose, to get item.
        return self

    def __iter__(self):
        # build iterator for priority queue to get first item of list, which is index to original list.
        return self.PriorityQueueIterator(self.array,len(self))

    # build iterator for priority queue to get first item of list, which is index to original list.
    class PriorityQueueIterator:
            def __init__(self, heapArray, numOfItem):
                self.current = heapArray
                self.maxItem = numOfItem
                #skip first element because it is a null value
                self.pointer = 1

            def __next__(self):
                #when pointer has reach maximum length of list or current item in heap array is none
                #Then, raise StopIteration to let programs knows its time to stop.
                if self.pointer > self.maxItem or self.current[self.pointer] == None:
                    raise StopIteration
                #when self.current still has item to iterate, add pointer by 1 and return current item which would consist index of original list.
                else:
                    wordIndex = self.current[self.pointer][0]
                    self.pointer += 1
                    return wordIndex

            def __iter__(self):
                return self

def kTopWords(kTop, listofList):
    """
    :param kTop: an integer that specify number of top item in array to be output
    :param listofList: contains list of words and its frequency
    :return: an array that contain top k item of array for list of words and frequency.
    Time Complexity:
            Best Case: O(klogk)
            Worst Case: O(nLogk)
            where n is number of item in original list and k is k is kth number of top-most frequent words.

            Best Case: Happens when first kth item is already in min-heap array data structure, rise() method is
            terminated as early as O(1) which result O(n) for first loops but delete-min still cost O(klogk) which cost
            O(klogk).Hence, time complexity for best case is resulting O(klogk).

            Worst Case: Happens when at each n iteration, new child nodes is needed to swap all the way
            to becomes parent nodes or new child nodes is already bigger than parent nodes or had higher index value
            for same word frequency which would takes O(nlogk). Then second loops for delete minimum operation
            would require the last node as root to shift all the way to leaf node which would
            takes o(klogk). Nonetheless, worst case comes when k reaches n, where all item is inserted to min heap, rise()
            method has to be called at n iteration and delete min will takes O(klogk) resulting O((n+k)logk) but k never reaches
            n so, at worst, it just double n values which results O(nlogk).

    Space Complexity:
            Best Case:  O(km)
            Worst Case: O(km)
            where m is maximum character of string and k is kth number of top-most frequent words.
            Best Case == Worst Case, this function will always needs km memory space to fit k item with m maximum character.
    """
    #return empty array when kTop is invalid number or list is empty
    if kTop <= 0 or len(listofList) < 1 : return []
    # initialise empty min heap.
    newHeap = MinHeap(kTop)
    #add counter for keeping track of index
    counter = 0
    #go through each item in list
    for item in listofList:
        #if length of new heap less than ktop,add item to heap.
        if len(newHeap) < kTop:
            newHeap.add(item[1], counter)
        #if frequency of current item in original list is more than minimum item in heap
        #   remove minimum item, then add current item to new heap.
        elif item[1] > newHeap.getmin():
            newHeap.extract()
            newHeap.add(item[1], counter)
        counter += 1
    #initialise empty array
    newArray = []
    #perform heap sort to make the heap contains descending order array.
    newHeap.setReverse()
    #append k item of original list based index in iterator of heaps to add in to new array.
    for index in newHeap:
        newArray.append(listofList[index])
    return newArray

if __name__ == '__main__':
    filename = 'Writing.txt'
    try:
        array = preprocess(filename)
        if len(array) == 0 : raise AssertionError
        print("Words are preprocessed..")
        askUserAnswer("Do I need to display the remaining words: ",array)
        wordSort(array)
        askUserAnswer("The remaining words are sorted in alphabetical order \n"+"Do you want to see: ",array)
        array = wordCount(array)
        print("The total number of words in the writing: "+ str(array.pop(0)))
        print("The frequencies of each word:")
        printWordAndCount(array)
        askUserAnswerK("How many top-most frequent words do I display: ",array)
    except FileNotFoundError as err:
        print(str(err))
    except AssertionError:
        print("Unable to continue: "+"\n"+"1. "+filename+" is empty or"+"\n"+"2. There is no word remaining after preprocessing.")
    except ValueError as err:
        print(str(err))

