import heapq
class Node:
    def __init__(self,char,freq):
        self.char=char
        self.freq=freq
        self.left=None
        self.right=None 
    
    def __lt__(self,other):
        return self.freq<other.freq
        
def huffman_coding(text):
    freq={}
    for i in text:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    print(freq)
    
    heap=[]
    for ch,fr in freq.items():
        heap.append(Node(ch,fr))
    heapq.heapify(heap)
    
    while len(heap)>1:
        left=heapq.heappop(heap)
        right=heapq.heappop(heap)
        new_node=Node(None,left.freq+right.freq)
        new_node.left=left
        new_node.right=right
        heapq.heappush(heap,new_node)
    root=heap[0]
    codes={}
    def generate_code(root,code):
        if root is None:
            return 
        if root.char is not None:
            codes[root.char]=code
            return 
        generate_code(root.left,code+"0")
        generate_code(root.right,code+"1")
    generate_code(root,"")
    
    print("Character\tFrequency\tCode")
    for ch in freq:
        print(f"{ch}\t\t\t{freq[ch]}\t\t\t{codes[ch]}")

    encoded_text = ""
    for ch in text:
        encoded_text = encoded_text + codes[ch]

    print("\nEncoded Text:", encoded_text)
    
a=input("enter string for encoding=")
huffman_coding(a)