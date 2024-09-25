import re

def extract_cpi(report):

    exec_blocks = re.findall(r"EXEC NAME: (.+?)\n.*?Real cycles: (\d+).*?Real instructions: (\d+)", report, re.DOTALL)

    for exec_name, cycles, instructions in exec_blocks:

        cycles = int(cycles)
        instructions = int(instructions)


        cpi = cycles / instructions if instructions != 0 else float('inf')


        print(f"{exec_name}: CPI = {cpi:.3f}")


report_data = """
EXEC NAME: aha-mont64
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 8968603
Real instructions: 4531262
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/aha-mont64.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/aha-mont64.irom8.hex
Simulation fast clock cycles (/1): 17980710
Simulation main clock cycles (/2): 8990355

------------------------------
           HART: 0
------------------------------
Cycles: 8990350
Time: 8990350
Retired instructions: 4542231
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: crc32
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 8707654
Real instructions: 3831160
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/crc32.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/crc32.irom8.hex
Simulation fast clock cycles (/1): 17518666
Simulation main clock cycles (/2): 8759333

------------------------------
           HART: 0
------------------------------
Cycles: 8759328
Time: 8759328
Retired instructions: 3853897
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: cubic
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 12736208
Real instructions: 6033867
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/cubic.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/cubic.irom8.hex
Simulation fast clock cycles (/1): 28022400
Simulation main clock cycles (/2): 14011200

------------------------------
           HART: 0
------------------------------
Cycles: 14011195
Time: 14011195
Retired instructions: 6637917
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: edn
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 7984984
Real instructions: 3999197
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/edn.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/edn.irom8.hex
Simulation fast clock cycles (/1): 16159686
Simulation main clock cycles (/2): 8079843

------------------------------
           HART: 0
------------------------------
Cycles: 8079838
Time: 8079838
Retired instructions: 4046574
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: huffbench
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6131950
Real instructions: 2598466
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/huffbench.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/huffbench.irom8.hex
Simulation fast clock cycles (/1): 13405256
Simulation main clock cycles (/2): 6702628

------------------------------
           HART: 0
------------------------------
Cycles: 6702623
Time: 6702623
Retired instructions: 2840277
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: matmult-int
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 7397094
Real instructions: 3183123
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/matmult-int.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/matmult-int.irom8.hex
Simulation fast clock cycles (/1): 15213594
Simulation main clock cycles (/2): 7606797

------------------------------
           HART: 0
------------------------------
Cycles: 7606792
Time: 7606792
Retired instructions: 3266799
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: md5sum
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 4193669
Real instructions: 2046781
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/md5sum.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/md5sum.irom8.hex
Simulation fast clock cycles (/1): 8562620
Simulation main clock cycles (/2): 4281310

------------------------------
           HART: 0
------------------------------
Cycles: 4281305
Time: 4281305
Retired instructions: 2089515
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: minver
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 12100254
Real instructions: 4964001
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/minver.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/minver.irom8.hex
Simulation fast clock cycles (/1): 24246168
Simulation main clock cycles (/2): 12123084

------------------------------
           HART: 0
------------------------------
Cycles: 12123079
Time: 12123079
Retired instructions: 4973402
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nbody
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 7875824
Real instructions: 3478553
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/nbody.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/nbody.irom8.hex
Simulation fast clock cycles (/1): 31501788
Simulation main clock cycles (/2): 15750894

------------------------------
           HART: 0
------------------------------
Cycles: 15750889
Time: 15750889
Retired instructions: 6957044
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nettle-aes
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6925173
Real instructions: 4463292
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/nettle-aes.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/nettle-aes.irom8.hex
Simulation fast clock cycles (/1): 14048978
Simulation main clock cycles (/2): 7024489

------------------------------
           HART: 0
------------------------------
Cycles: 7024484
Time: 7024484
Retired instructions: 4526639
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nettle-sha256
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6249208
Real instructions: 4030435
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/nettle-sha256.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/nettle-sha256.irom8.hex
Simulation fast clock cycles (/1): 12527652
Simulation main clock cycles (/2): 6263826

------------------------------
           HART: 0
------------------------------
Cycles: 6263821
Time: 6263821
Retired instructions: 4039634
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: nsichneu
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 7077095
Real instructions: 2236759
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/nsichneu.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/nsichneu.irom8.hex
Simulation fast clock cycles (/1): 14167362
Simulation main clock cycles (/2): 7083681

------------------------------
           HART: 0
------------------------------
Cycles: 7083676
Time: 7083676
Retired instructions: 2238947
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: picojpeg
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 7809173
Real instructions: 4171077
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/picojpeg.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/picojpeg.irom8.hex
Simulation fast clock cycles (/1): 18226748
Simulation main clock cycles (/2): 9113374

------------------------------
           HART: 0
------------------------------
Cycles: 9113369
Time: 9113369
Retired instructions: 4867396
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: primecount
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6223074
Real instructions: 2148523
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/primecount.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/primecount.irom8.hex
Simulation fast clock cycles (/1): 24893044
Simulation main clock cycles (/2): 12446522

------------------------------
           HART: 0
------------------------------
Cycles: 12446517
Time: 12446517
Retired instructions: 4297207
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: qrduino
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 6081388
Real instructions: 3169184
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/qrduino.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/qrduino.irom8.hex
Simulation fast clock cycles (/1): 14615284
Simulation main clock cycles (/2): 7307642

------------------------------
           HART: 0
------------------------------
Cycles: 7307637
Time: 7307637
Retired instructions: 3807579
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: sglib-combined
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6384821
Real instructions: 2628017
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/sglib-combined.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/sglib-combined.irom8.hex
Simulation fast clock cycles (/1): 13252552
Simulation main clock cycles (/2): 6626276

------------------------------
           HART: 0
------------------------------
Cycles: 6626271
Time: 6626271
Retired instructions: 2726386
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: slre
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 6088582
Real instructions: 2590543
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/slre.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/slre.irom8.hex
Simulation fast clock cycles (/1): 12289162
Simulation main clock cycles (/2): 6144581

------------------------------
           HART: 0
------------------------------
Cycles: 6144576
Time: 6144576
Retired instructions: 2614381
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: st
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 8884972
Real instructions: 3936305
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/st.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/st.irom8.hex
Simulation fast clock cycles (/1): 19142844
Simulation main clock cycles (/2): 9571422

------------------------------
           HART: 0
------------------------------
Cycles: 9571417
Time: 9571417
Retired instructions: 4240433
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: statemate
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 2457030
Real instructions: 1317876
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/statemate.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/statemate.irom8.hex
Simulation fast clock cycles (/1): 4919866
Simulation main clock cycles (/2): 2459933

------------------------------
           HART: 0
------------------------------
Cycles: 2459928
Time: 2459928
Retired instructions: 1319407
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: tarfind
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 3027137
Real instructions: 1037257
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/tarfind.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/tarfind.irom8.hex
Simulation fast clock cycles (/1): 6204272
Simulation main clock cycles (/2): 3102136

------------------------------
           HART: 0
------------------------------
Cycles: 3102131
Time: 3102131
Retired instructions: 1064151
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: ud
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 8210396
Real instructions: 3358071
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/ud.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/ud.irom8.hex
Simulation fast clock cycles (/1): 16436320
Simulation main clock cycles (/2): 8218160

------------------------------
           HART: 0
------------------------------
Cycles: 8218155
Time: 8218155
Retired instructions: 3361307
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------

EXEC NAME: wikisort
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 3083100
Real instructions: 1265262
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/wikisort.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010FIFNoNlpNoHpmMulRegDiv2/wikisort.irom8.hex
Simulation fast clock cycles (/1): 12385994
Simulation main clock cycles (/2): 6192997

------------------------------
           HART: 0
------------------------------
Cycles: 6192992
Time: 6192992
Retired instructions: 2540082
ALU instructions: 0
BRU instructions: 0
MUL instructions: 0
DIV instructions: 0
Load instructions: 0
Store instructions: 0
BR instructions: 0
BR forward instructions: 0
BR backward instructions: 0
JAL instructions: 0
JALR instructions: 0
CALL instructions: 0
RET instructions: 0
Read cycle instructions: 0
Cache flush instructions: 0
16-bit instructions: 0
32-bit instructions: 0
0 read port: 0
1 read port: 0
2 read port: 0
Taken BR: 0
Taken BR forward: 0
Taken BR backward: 0
Not taken BR: 0
Not taken BR forward: 0
Not taken BR backward: 0
Mispredicted instructions: 0
Mispredicted BR: 0
Mispredicted BR taken: 0
Mispredicted BR forward taken: 0
Mispredicted BR backward taken: 0
Mispredicted BR not taken: 0
Mispredicted BR forward not taken: 0
Mispredicted BR backward not taken: 0
Mispredicted JALR: 0
Mispredicted CALL: 0
Mispredicted RET: 0
Partial instructions: 0
Instruction buffer full: 0
Instruction buffer dead: 0
Wait source dependency: 0
Wait MUL unit: 0
Wait DIV unit: 0
Wait data request: 0
Wait data acknowledgement: 0
Empty buffer for misaligned instructions: 0
Empty fetch port: 0
Empty commit port: 0
L1I hits: 0
L1I misses: 0
L1I prefetches: 0
L1D hits: 0
L1D misses: 0
L1D prefetches: 0
L2 hits: 0
L2 misses: 0
L2 prefetches: 0
------------------------------


"""

extract_cpi(report_data)
