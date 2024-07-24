import re

def extract_cpi(report):

    exec_blocks = re.findall(r"EXEC NAME: (.+?)\n.*?Real instructions: (\d+)", report, re.DOTALL)

    for exec_name,  instructions in exec_blocks:

        instructions = int(instructions)


      


        print(f"{exec_name}: instr number = {instructions}")


report_data = """

EXEC NAME: aha-mont64
[1;32mTEST REPORT: SUCCESS.[0m
Real cycles: 8678816
Real instructions: 4531262
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/aha-mont64.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/aha-mont64.irom8.hex
Simulation fast clock cycles (/1): 17399878
Simulation main clock cycles (/2): 8699939

------------------------------
           HART: 0
------------------------------
Cycles: 8699934
Time: 8699934
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
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 6794310
Real instructions: 3831161
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/crc32.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/crc32.irom8.hex
Simulation fast clock cycles (/1): 13669554
Simulation main clock cycles (/2): 6834777

------------------------------
           HART: 0
------------------------------
Cycles: 6834772
Time: 6834772
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
Real cycles: 12544193
Real instructions: 5804239
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/cubic.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/cubic.irom8.hex
Simulation fast clock cycles (/1): 27600350
Simulation main clock cycles (/2): 13800175

------------------------------
           HART: 0
------------------------------
Cycles: 13800170
Time: 13800170
Retired instructions: 6385409
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
Real cycles: 6268306
Real instructions: 4026254
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/edn.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/edn.irom8.hex
Simulation fast clock cycles (/1): 12687010
Simulation main clock cycles (/2): 6343505

------------------------------
           HART: 0
------------------------------
Cycles: 6343500
Time: 6343500
Retired instructions: 4073941
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
Real cycles: 5720968
Real instructions: 2598466
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/huffbench.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/huffbench.irom8.hex
Simulation fast clock cycles (/1): 12507546
Simulation main clock cycles (/2): 6253773

------------------------------
           HART: 0
------------------------------
Cycles: 6253768
Time: 6253768
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
Real cycles: 5781309
Real instructions: 3183123
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/matmult-int.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/matmult-int.irom8.hex
Simulation fast clock cycles (/1): 11898902
Simulation main clock cycles (/2): 5949451

------------------------------
           HART: 0
------------------------------
Cycles: 5949446
Time: 5949446
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
Real cycles: 4027930
Real instructions: 2046781
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/md5sum.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/md5sum.irom8.hex
Simulation fast clock cycles (/1): 8225308
Simulation main clock cycles (/2): 4112654

------------------------------
           HART: 0
------------------------------
Cycles: 4112649
Time: 4112649
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
Real cycles: 12691555
Real instructions: 4964001
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/minver.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/minver.irom8.hex
Simulation fast clock cycles (/1): 25431014
Simulation main clock cycles (/2): 12715507

------------------------------
           HART: 0
------------------------------
Cycles: 12715502
Time: 12715502
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
Real cycles: 8052378
Real instructions: 3484767
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/nbody.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/nbody.irom8.hex
Simulation fast clock cycles (/1): 32205842
Simulation main clock cycles (/2): 16102921

------------------------------
           HART: 0
------------------------------
Cycles: 16102916
Time: 16102916
Retired instructions: 6969472
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
Real cycles: 6987414
Real instructions: 4462473
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/nettle-aes.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/nettle-aes.irom8.hex
Simulation fast clock cycles (/1): 14174042
Simulation main clock cycles (/2): 7087021

------------------------------
           HART: 0
------------------------------
Cycles: 7087016
Time: 7087016
Retired instructions: 4525936
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
Real cycles: 6320308
Real instructions: 4030435
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/nettle-sha256.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/nettle-sha256.irom8.hex
Simulation fast clock cycles (/1): 12670254
Simulation main clock cycles (/2): 6335127

------------------------------
           HART: 0
------------------------------
Cycles: 6335122
Time: 6335122
Retired instructions: 4039637
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
Real cycles: 8268709
Real instructions: 2236759
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/nsichneu.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/nsichneu.irom8.hex
Simulation fast clock cycles (/1): 16552628
Simulation main clock cycles (/2): 8276314

------------------------------
           HART: 0
------------------------------
Cycles: 8276309
Time: 8276309
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
Real cycles: 7583514
Real instructions: 4196163
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/picojpeg.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/picojpeg.irom8.hex
Simulation fast clock cycles (/1): 17692062
Simulation main clock cycles (/2): 8846031

------------------------------
           HART: 0
------------------------------
Cycles: 8846026
Time: 8846026
Retired instructions: 4896836
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
Real cycles: 6108589
Real instructions: 2148523
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/primecount.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/primecount.irom8.hex
Simulation fast clock cycles (/1): 24435240
Simulation main clock cycles (/2): 12217620

------------------------------
           HART: 0
------------------------------
Cycles: 12217615
Time: 12217615
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
Real cycles: 5925071
Real instructions: 3174005
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/qrduino.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/qrduino.irom8.hex
Simulation fast clock cycles (/1): 14240432
Simulation main clock cycles (/2): 7120216

------------------------------
           HART: 0
------------------------------
Cycles: 7120211
Time: 7120211
Retired instructions: 3813331
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
Real cycles: 6410931
Real instructions: 2624376
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/sglib-combined.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/sglib-combined.irom8.hex
Simulation fast clock cycles (/1): 13307326
Simulation main clock cycles (/2): 6653663

------------------------------
           HART: 0
------------------------------
Cycles: 6653658
Time: 6653658
Retired instructions: 2722619
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
Real cycles: 6505559
Real instructions: 2590543
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/slre.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/slre.irom8.hex
Simulation fast clock cycles (/1): 13130716
Simulation main clock cycles (/2): 6565358

------------------------------
           HART: 0
------------------------------
Cycles: 6565353
Time: 6565353
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
Real cycles: 9087354
Real instructions: 3931417
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/st.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/st.irom8.hex
Simulation fast clock cycles (/1): 19578976
Simulation main clock cycles (/2): 9789488

------------------------------
           HART: 0
------------------------------
Cycles: 9789483
Time: 9789483
Retired instructions: 4235169
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
Real cycles: 2671128
Real instructions: 1318856
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/statemate.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/statemate.irom8.hex
Simulation fast clock cycles (/1): 5347916
Simulation main clock cycles (/2): 2673958

------------------------------
           HART: 0
------------------------------
Cycles: 2673953
Time: 2673953
Retired instructions: 1320387
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
Real cycles: 2480766
Real instructions: 1037257
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/tarfind.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/tarfind.irom8.hex
Simulation fast clock cycles (/1): 5089582
Simulation main clock cycles (/2): 2544791

------------------------------
           HART: 0
------------------------------
Cycles: 2544786
Time: 2544786
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
Real cycles: 8609522
Real instructions: 3358071
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/ud.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/ud.irom8.hex
Simulation fast clock cycles (/1): 17235448
Simulation main clock cycles (/2): 8617724

------------------------------
           HART: 0
------------------------------
Cycles: 8617719
Time: 8617719
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
[1;31mTEST REPORT: FAILED.[0m
Real cycles: 3056374
Real instructions: 1267935
BOOT file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/wikisort.boot8.hex
iROM file: /home/mrabiai/Bureau/herd-ware/sw/embench-iot/hex/SIM/WAESP32AU1V010NoHpm2Btb16IFReg/wikisort.irom8.hex
Simulation fast clock cycles (/1): 12281206
Simulation main clock cycles (/2): 6140603

------------------------------
           HART: 0
------------------------------
Cycles: 6140598
Time: 6140598
Retired instructions: 2539847
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
