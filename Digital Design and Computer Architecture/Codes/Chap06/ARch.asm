# Register Operands

# $s0 = a, $s1 = b, $s2 = c 
add $s0, $s1, $s2            # a = b + c


# Temporary Registers
# $s0 = a, $s1 = b, $s2 = c, $s3 = d

sub $t0, $s2, $s3       # t =  c - d
add $s0, $s1, $t0       # a = b + t 