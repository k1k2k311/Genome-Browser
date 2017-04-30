import Regexes_full

import parser_re

import res




codon_s = Regexes_full.p_codon_start


# p_codon_end is needed in regexes_full

codon_e = Regexes_full.p_codon_end

# related with precal.py

extract_seq= Regexes_full.p_trans


re_site=res.single_res(extract_seq)

# expected result [(enzyme, start,end),(enzyme,start,end)...]


def good_bad():
    for k in re_site:
        if k[2]>codon_s and re_site[3]<codon_e:
            return print("good")
        else:
            return print ("bad") 
# test

codon_s=1588
codon_e=3588
re_site=[('BAMHI','245','348'),('BAMHI,1023,1028')]

print(good_bad())
