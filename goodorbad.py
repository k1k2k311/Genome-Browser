#Gathering information from data_access file 

import database.data_access

# restriction enzyme site finding file 

import res

# Start site of coding region
coding_s = data_access.get_full_seq_and_position()[1]

# End site of coding region
coding_e = data_access.get_full_seq_and_position()[2]

# check weather 5' end is partial 
partial5 = data_access. get_full_seq_and_positions()[3]

# check weather 3' end is partial 
partial3 = data_access. get_full_seq_and_positions()[4]


# get_full_seq_andpositions() returns [full_seq, coding_start, coding_end, partial_5, partial_3] format


extract_seq = data_access.get_ful_seq_and_position()[0]


# will find restriction enzyme site of which enzyme,  you want to figure out it is good or bad.

re_site=res.single_res('enzyme',extract_seq)

# expected result [(enzyme, start,end),(enzyme,start,end)...]
 
 
 
# First we set bad as false

# If any restirction enzyme site is bad(between x),for loop is broken
# and bad is returned, otherwise the site is deem to be good

def good_bad():
    bad = False
    if partial3=="no" and partial5=="no":
        for k in re_site:
            if (int(k[1])>codon_s and int(k[2])<codon_e):
                return ("bad")
                bad = True
                break
            else:
                pass
        if not bad:
            return ("good")

    else:
        return("Since (one of them/both)are partial end, we could not figure it out it is good or bad")

     
# test
     
partial3= 'no'
partial5= 'yes'
codon_s=1588
codon_e=3588
re_site=[('BAMHI','150','220'),('BAMHI','1023','1028')]

print(good_bad())
               


