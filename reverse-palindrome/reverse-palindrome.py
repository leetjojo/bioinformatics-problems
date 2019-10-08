from Bio import SeqIO

output = open("output-example.txt","w+")
def findPalindrome(seq, reverseSeq):
    for i in range(0, len(seq)):
        for j in range(i+4, i+13):
            start = len(seq)-j
            end = len(seq)-i
            if (len(seq) >= (j)):
                if (seq[i:j] == reverseSeq[start:end]):
                    output.write("{} {}\n".format(i+1, j-i))

for record in SeqIO.parse("input-example.fasta", "fasta"):
    findPalindrome(record.seq, record.reverse_complement().seq)
