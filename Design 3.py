import numpy as np
import time

def erasure_code(data):
  data_temp = []
  for i in range(12):
    data_temp.append([data[i]])
  mat_data = np.mat(data_temp)
  mat_enc = np.mat([[1,0,0,0,0,0,0,0,0,0,0,0],
  [0,1,0,0,0,0,0,0,0,0,0,0],
  [0,0,1,0,0,0,0,0,0,0,0,0],
  [0,0,0,1,0,0,0,0,0,0,0,0],
  [0,0,0,0,1,0,0,0,0,0,0,0],
  [0,0,0,0,0,1,0,0,0,0,0,0],
  [0,0,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,0,0,0,0],
  [0,0,0,0,0,0,0,0,1,0,0,0],
  [0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0],
  [0,0,0,0,0,0,0,0,0,0,0,1],
  [1^0,1^1,1^2,1^3,1^4,1^5,1^6,1^7,1^8,1^9,1^10,1^11],
  [2^0,2^1,2^2,2^3,2^4,2^5,2^6,2^7,2^8,2^9,2^10,2^11],
  [3^0,3^1,3^2,3^3,3^4,3^5,3^6,3^7,3^8,3^9,3^10,3^11],
  [4^0,4^1,4^2,4^3,4^4,4^5,4^6,4^7,4^8,4^9,4^10,4^11]])
  mat_mes = np.dot(mat_enc, mat_data)
  mat_mes[12][0] = mat_mes[12][0] % 256
  mat_mes[13][0] = mat_mes[13][0] % 256
  mat_mes[14][0] = mat_mes[14][0] % 256
  mat_mes[15][0] = mat_mes[15][0] % 256
  return mat_mes

filename = input("Please input file name to be encoded:")
with open(filename, "rb") as f:
  data = f.read()

start_time = time.time()
for i in range(0, 307200, 48):
  data1 = data[i:i+12]
  data2 = data[i+12:i+24]
  data3 = data[i+24:i+36]
  data4 = data[i+36:i+48]

  mat_mes1 = erasure_code(data1)
  mat_mes2 = erasure_code(data2)
  mat_mes3 = erasure_code(data3)
  mat_mes4 = erasure_code(data4)
  mat_mes3[13][0] = (mat_mes3[13][0] + mat_mes1[12][0] + mat_mes1[15][0] + mat_mes2[14][0]) % 256
  mat_mes4[13][0] = (mat_mes3[13][0] + mat_mes1[14][0] + mat_mes2[12][0] + mat_mes2[15][0]) % 256
  mat_mes3[14][0] = (mat_mes3[14][0] + mat_mes1[0][0] + mat_mes1[4][0] + mat_mes1[8][0]
   + mat_mes2[0][0] + mat_mes2[4][0] + mat_mes2[8][0]) % 256
  mat_mes3[15][0] = (mat_mes3[15][0] + mat_mes1[1][0] + mat_mes1[5][0] + mat_mes1[9][0]
   + mat_mes2[1][0] + mat_mes2[5][0] + mat_mes2[9][0]) % 256
  mat_mes4[14][0] = (mat_mes4[14][0] + mat_mes1[2][0] + mat_mes1[6][0] + mat_mes1[10][0]
   + mat_mes2[2][0] + mat_mes2[6][0] + mat_mes2[10][0]) % 256
  mat_mes4[15][0] = (mat_mes4[15][0] + mat_mes1[3][0] + mat_mes1[7][0] + mat_mes1[11][0]
   + mat_mes2[3][0] + mat_mes2[7][0] + mat_mes2[11][0]) % 256
  filename_list = ["output1.txt",
  "output2.txt",
  "output3.txt",
  "output4.txt",
  "output5.txt",
  "output6.txt",
  "output7.txt",
  "output8.txt",
  "output9.txt",
  "output10.txt",
  "output11.txt",
  "output12.txt",
  "output13.txt",
  "output14.txt",
  "output15.txt",
  "output16.txt"]
  for j in range(16):
    with open(filename_list[j], "ab") as f1:
      f1.write(int(mat_mes1[j][0]).to_bytes(length=1, byteorder='big', signed=False))
      f1.write(int(mat_mes2[j][0]).to_bytes(length=1, byteorder='big', signed=False))
      f1.write(int(mat_mes3[j][0]).to_bytes(length=1, byteorder='big', signed=False))
      f1.write(int(mat_mes4[j][0]).to_bytes(length=1, byteorder='big', signed=False))
end_time = time.time()
print(f"Time used: {end_time-start_time}s")