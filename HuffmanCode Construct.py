import heapq
#--------------Loading txt file into frequency dictionary--------
#Commented out file loading because it's unnecessary 
'''file=open("Metamorphosis.txt", "r")
content=file.read()
freq_dict={}
for i in content:
    if i not in freq_dict:
        freq_dict[i]=1
    else:
        freq_dict[i]+=1'''

#------HuffmanNode Class--------
class HuffmanNode(object):
    def __init__(self, freq=None,char=None,left=None,right=None):
        self.freq=freq
        self.char=char
        self.left=left
        self.right=right
    def __lt__(self, other):
        return self.freq < other.freq


#-------Frequency List------
#freq=sorted([(fre,char) for char, fre in freq_dict.items()])
#At first I started with every character the source file had
#Clean_freq is the list that has only 32 valid characters 
clean_freq=sorted([(21, 'z'),(43, '!'), (55, '?'), (91, 'j'), (92, 'q'), (99, 'x'),
             (331, "'"), (738, '.'),(771, 'k'), (826, 'v'), (1268, 'p'), (1296, ','), (1383, 'b'), (1633, 'y'), (1926, 'c'),(2107, 'f'), (2297, 'm'), (2367, 'g'),
             (2372, 'w'), (2473, 'u'), (3940, 'l'), (4193, 'd'), (5474, 'r'), (5693, 's'), (5921, 'n'), (6007, 'i'), (7072, 'a'), (7105, 'h'),
                   (7482, 'o'), (9042, 't'), (11918, 'e'), (20882, ' ')])


#------Building Huffman Tree-------
def hufftree(freq_ls):
    q=[]
    for i in freq_ls:
      node=HuffmanNode()
      node.char=i[1]
      node.freq=i[0]
      heapq.heappush(q,(node.freq, node))
    while len(q)>1:
        right=heapq.heappop(q)
        left=heapq.heappop(q)
        newnode=HuffmanNode()
        newnode.char=left[1].char+right[1].char
        newnode.freq=left[1].freq+right[1].freq
        newnode.left=left[1]
        newnode.right=right[1]
        #print(newnode.left,"left---------------")
        #print(newnode.right,"right----------------")
        heapq.heappush(q,(newnode.freq,newnode))
    return q
#tree=hufftree(freq)
#print(tree)


#------Traversing tree with 0 & 1----- 
def traverse(node,bit):
    if node.left is None and node.right is None:
        print(node.char,bit)
    else:
        traverse(node.left,bit+'0')
        traverse(node.right,bit+'1')
    
#code=traverse(tree[0][1],'')
#print(code)
#----Main------
clean_tree=hufftree(clean_freq)
clean_code=traverse(clean_tree[0][1],'')
fixedbit=0
for i in clean_freq:
    fixedbit+=i[0]*5
output="The text was encoded using 492167 bits in Huffman Coding \n"
output+="I used 32 characters to encode \n"
output+="Using a 5-bit fixed length encoding, this would have been "+str(fixedbit)+" bits long \n"
output+="We saved "+str(fixedbit-492167)+" bits. That's 11.552875 Kb"
print(output)

#total bits using huffman=492167
#5bit fixed length =584590
