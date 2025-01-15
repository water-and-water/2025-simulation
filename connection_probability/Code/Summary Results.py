import numpy as np


# 使用嵌套列表来表示2x2矩阵
# 格式是（layer23-layer23，layer23-layer5；layer5-layer23，layer5-layer5）,(neuron_num,bouton_num,axon_length)
matrices = {
    'VIS_VIS': [
        [(33,9659,162870.18), (33,6950,142224.345)],
        [(14,532,12477.867), (14,4103,62742.088)]
    ],
    'SS_SS': [
        [(28,1729,38315.821), (28,1419,32143.152)],
        [(172,323,6760.702), (172,7753,125429.312)]
    ],

    'EFC_EFC': [
        [(38,29386,566661.71), (38,24897,493455.469)],
        [(35,4359,106192.836), (35,10116,247688.597)]
    ],
    'MC_MC': [
        [(9,2802,51602.112), (9,3063,60634.943)],
        [(30,4659,86593.731), (30,12469,254295.684)]
    ]
}

# 打印矩阵
for label, matrix in matrices.items():
    print(f"Matrix {label}:\n{matrix}")

# 将字典中的每个矩阵转换为NumPy数组
numpy_matrices = {label: np.array(matrix) for label, matrix in matrices.items()}
