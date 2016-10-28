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


# Accessing Byte-Addressable Memory

lw $s0, 0($0)       # read data word 0 (0xABCDEF78) into $s0
lw $s1, 8($0)       # read data word 2 (0x01EE2842) into $s1 
lw $s2, 0xC($0)     # read data word 3 (0x40F30788) into $s2

sw $s3, 4($0)       # write $s3 to data word 1
sw $s4, 0x20($0)    # write $s4 to data word 8
sw $s5, 400($0)     # write $s5 to data word 100



# Immediate Operands

# $s0 = a, $s1 = b
addi	$s0, $s0, 4		# a = a + 4
addi    $s1, $s0, - 12  # b = a - 12


