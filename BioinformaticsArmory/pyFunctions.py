##############################################################################
##
##             Introduction to Bioinformatics
##
##############################################################################

### Counting Nucleotides
def countingNucleotides(sequence):
    nucleotides = {}
    for nucl in sequence:
        if nucl not in nucleotides.keys():
            nucleotides[nucl] = 1
        else:
            nucleotides[nucl] += 1
    return nucleotides

from Bio.Seq import Seq
from time import time

if __name__ == "__main__":
  sequence = "CTACATGCCGACATCCATGCCGTAGTGACTATTTTATGATAGGTGTTCGGACATCCACCA" + \
             "CAATCTGACCAGCGAGTTCGGGCTTCCTTCAACTAATCTTGAATCCATCATCAACCTCGT" + \
             "GTTAATAGAACGAATTATTTCGTACTTACTTCACCCTAGCCCTTATGGTTTACCCGGCAC" + \
             "CTGACTAAAGCTAACGCCCTACTCGCCTAGCCTGCCCATTAACCCCATTCGATGCAGATG" + \
             "CAACTATACTGTGCCTAGCGAAACTCGCCCGCTGGCATGAAAAGAACATAGTCCTTACCT" + \
             "TAGTGAGCGCACGACACGATCACACATCGAGGGTGGTCGGTTTGTCTAGGAGCGCGTGAC" + \
             "AATAAAATTTTCTCATAGTTCTATGTTTTGCGGCACTTAGCTTTCGCCCCTCGGTGCGCG" + \
             "AGAATTCTAGACCATGCGTAATCAAAAACTTCTGGGAAGAAGCACCTAAATAATCCAAAA" + \
             "ACTAACACCTGGTACAAACTTAGCAATACACAGGCTAGACGATTCGTAGAATGCCTATCG" + \
             "GTCACGGTAGAGCAATCATGTTATTTTAGCATCTCTATAAGTCTTTTTCGACGGCTACAT" + \
             "CGTTATATATGGGTATTGTCCCATCATTACGAAAATTGCGGCGGCCTGATATATTCTATT" + \
             "GGGCATATTGAGACAAAGCCATCAGAACTACGGCTTCGCATGTGTGGTCTACTATGTTGT" + \
             "AGGACCTGGGATAAACATAATCCTTGCTTCGTTTTTAAGTAGCAGCCGACTCAAACCCTG" + \
             "CCCTATCAGCAACAGTCCTCTGTTCCAGTTAAAGAAAGGTACAACAAGCTGATCAGTTAG" + \
             "GACGCCGGAAAACAAACTAAACGACCCGCGGTAATACCGGCGAAATTGGGGGAGGCGTCA" + \
             "ATGTTCTAAAGGGACTGAGATATAGAAACGACTAACCAGTAGGTTCACACGACTCACGTG" + \
             "TTATGCTTAGTTCTAGCGACT"
  time1 = time()
  print(" ".join([str(i) for i in countingNucleotides(sequence).values()]))
  time2 = time()
  ###### The biopythonic way
  bioSequence = Seq(sequence)
  nucleotideList = [bioSequence.count("A"),
                    bioSequence.count("C"),
                    bioSequence.count("G"),
                    bioSequence.count("T")]
  print(" ".join([str(x) for x in nucleotideList]))
  time3 = time()
  print("The diference between the two times:\t" + \
        str(time2 - time1) + " (The normal way)\t" + \
        str(time3 - time2) + " (The biopythonic  way)")
