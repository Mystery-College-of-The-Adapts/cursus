# Register Operands

# $s0 = a, $s1 = b, $s2 = c 
add $s0, $s1, $s2            # a = b + c


# Temporary Registers
# $s0 = a, $s1 = b, $s2 = c, $s3 = d

sub $t0, $s2, $s3       # t =  c - d
add $s0, $s1, $t0       # a = b + t 



# Reading Word-Addressable Memory

lw $s3, 1($0)    # read memory word 1 into $3


# Writing Word-Addressable Memory

sw $s7, 5($0)    # Write $s7 to memory word 5 

