'''
Created on 24/11/2014

@author: Flavio Lichtenstein
'''
import classes.Timing as timePack
from tests import test_Class as TC

tc = TC.test_Class()

tc.frame = 0


time = timePack.Timing()    

'''
stri1 = 'ATGTCGTTTACTTTGACCAACAAGAACGTGATTTTCGTTGCCGGTCTGGGAGGCATTGGTCTGGACACCAGCAAGGAGCTGCTCAAGCGCGATCTGAAGGTAACTATGCGATGCCCACAGGCTCCATGCAGCGATGGAGGTTAATCTCGTGTATTCAATCCTAGAACCTGGTGATCCTCGACCGCATTGAGAACCCGGCTGCCATTGCCGAGCTGAAGGCAATCAATCCAAAGGTGACCGTCACCTTCTACCCCTATGATGTGACCGTGCCCATTGCCGAGACCACCAAGCTGCTGAAGACCATCTTCGCCCAGCTGAAGACCGTCGATGTCCTGATCAACGGAGCTGGTATCCTGGACGATCACCAGATCGAGCGCACCATTGCCGTCAACTACACTGGCCTGGTCAACACCACGACGGCCATTCTGGACTTCTGGGACAAGCGCAAGGGCGGTCCCGGTGGTATCATCTGCAACATTGGATCCGTCACTGGATTCAATGCCATCTACCAGGTGCCCGTCTACTCCGGCACCAAGGCCGCCGTGGTCAACTTCACCAGCTCCCTGGCGGTAAGTTGATCAAAGGAAACGCAAAGTTTTCAAGAAAAAACAAAACTAATTTGATTTATAACACCTTTAGAAACTGGCCCCCATTACCGGCGTGACGGCTTACACTGTGAACCCCGGCATCACCCGCACCACCCTGGTGCACACGTTCAACTCCTGGTTGGATGTTGAGCCTCAGGTTGCCGAGAAGCTCCTGGCTCATCCCACCCAGCCCTCGTTGGCCTGCGCCGAGAACTTCGTCAAGGCTATCGAGCTGAACCAGAACGGAGCCATCTGGAAACTGGACTTGGGCACCCTGGAGGCCATCCAGTGGACCAAGCACTGGGACTCCGGCATCTAA'
stri2 = 'ATGTCGTTTACTTTGACCAACAAGAACGTGATTTTCGTTGCCGGTCTGGGAGGCATTGGTCTGGACACCAGCAAGGAGCTGCTCAAGCGCGATCTGAAGGTAACTATGCGATGCCCACAGGCTCCATGCAGCGATGGAGGTTAATCTCGTGTATTCAATCCTAGAACCTGGTGATCCTCGACCGCATTGAGAACCCGGCTGCCATTGCCGAGCTGAAGGCAATCAATCCAAAGGTGACCGTCACCTTCTACCCCTATGATGTGACCGTGCCCATTGCCGAGACCACCAAGCTGCTGAAGACCATCTTCGCCCAGCTGAAGACCGTCGATGTCCTGATCAACGGAGCTGGTATCCTGGACGATCACCAGATCGAGCGCACCATTGCCGTCAACTACACTGGCCTGGTCAACACCACGACGGCCATTCTGGACTTCTGGGACAAGCGCAAGGGCGGTCCCGGTGGTATCATCTGCAACATTGGATCCGTCACTGGATTCAATGCCATCTACCAGGTGCCCGTCTACTCCGGCACCAAGGCCGCCGTGGTCAACTTCACCAGCTCCCTGGCGGTAAGTTGATCAAAGGAAACGCAAAGTTTTCAAGAAAAAACAAAACTAATTTGATTTATAACACCTTTAGAAACTGGCCCCCATTACCGGCGTGACCGCTTACACCGTGAACCCCGGCATCACCCGCACCACCCTGGTGCACAAGTTCAACTCCTGGTTGGATGTTGAGCCCCAGGTTGCTGAGAAGCTCCTGGCTCATCCCACCCAGCCATCGTTGGCCTGCGCCGAGAACTTCGTCAAGGCTATCGAACTGAACCAGAACGGAGCCATCTGGAAACTGGACTTGGGCACCCTGGAGGCCATCCAGTGGACCAAGCACTGGGACTCCGGCATCTAA'
seqs = []
seqs.append(stri1)
seqs.append(stri2)
'''

striNuc = 'AGTCAAAAAT'+'AGTCAAAAAT'[::-1]
striNuc = 'AGTCAAAAAT'
striNuc = 'AGTCAAAAAT'*3+'CGCGCG'

seqs = [striNuc for i in range(2)]


time.start()

tc.numOfLetters = 1
arrayMI, arrayMiInf, arraySE, arraySEcorr, arrayN = tc.run_hmi(seqs=seqs)

time.finish()
print time.milli(), 'ms'

print 'arrayMI=%s ' %(str(arrayMI))
print 'arrayMIinf=%s ' %(str(arrayMiInf))
print 'arraySE=%s ' %(str(arraySE))
print 'arraySEcorr=%s ' %(str(arraySEcorr))
print 'arrayN=%s ' %(str(arrayN))

