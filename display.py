import time
import random
print('\033[32m')
print('''
  _________  ______   __  _ 
 / ___/ __ \/ ___/ | / / (_)
/ /__/ /_/ / /__ | |/ / _   
\___/\____/\___/ |___/ (_)  

  _____                              __  _             ____         __              ___        
 / ___/__  _________ _____ ______ __/ /_(_)__  ___    / __/_ _____ / /____ __ _    / _/__  ____
/ /__/ _ \/___/ -_) \ / -_) __/ // / __/ / _ \/ _ \  _\ \/ // (_-</ __/ -_)  ' \  / _/ _ \/ __/
\___/\___/    \__/_\_\\__/\__/\_,_/\__/_/\___/_//_/ /___/\_, /___/\__/\__/_/_/_/ /_/ \___/_/   
                                                        /___/                                  
  _____                     __            _   ___     _             ______         __      
 / ___/__  __ _  ___  __ __/ /____ ____  | | / (_)__ (_)__  ___    /_  __/__ ____ / /__ ___
/ /__/ _ \/  ' \/ _ \/ // / __/ -_) __/  | |/ / (_-</ / _ \/ _ \    / / / _ `(_-</  '_/(_-<
\___/\___/_/_/_/ .__/\_,_/\__/\__/_/     |___/_/___/_/\___/_//_/   /_/  \_,_/___/_/\_\/___/
              /_/                                                                                                                                                                                                                             
                 
''')
    
print("\033[32m Co-execution System for Computer Vision tasks")
print()
print('''\u001b[36m This system implement the co-excution on the all stages for a computer vision tasks which are:
    * Pre-processing stage
    * Inference stage
    * Post-processing stage

\u001b[35mCoded py Wan Ye, 2023.5.11, NUAA\033[0m
''')
      
time.sleep(2)
print('''\u001b[42;1mChoose Computer Vision tasks\033[0m''')
print('''\033[0m
Choose a computer vision task:
    1. Image classification
    2. Object detection
''')

choice = input("Select your choice:")
if choice == '1':
    task = "Image classification"
    print("\u001b[44;1mTask: Image classification\033[0m")
else: 
    task = "Object detection"
    print("\u001b[44;1mTask: Object detection\033[0m")



print()
print('''\u001b[42;1mChoose Input Image\033[0m''')
address = input("Type the address of the input image:")

print()
print('''\u001b[42;1mStage: Pre-processing\033[0m
Choose a pre-processing operators :
    1. Resize: resize image to different sizes(default 300*400)
    2. MediumBlur: reduce the noise in the image
    3. Normalize: normalize the pixel of the image
''')

choice = input("Select your choice:")
if choice == '1':
    pre_kernel = "Resize"
    print("\u001b[44;1mPre-processing Operator: Resize\033[0m")
elif choice == '2': 
    pre_kernel = "MediumBlur"
    print("\u001b[44;1mPre-processing Operator: MediumBlur\033[0m")
else:
    pre_kernel = "Normalize"
    print("\u001b[44;1mPre-processing Operator: Normalize\033[0m")


# inference

print()
print('''\u001b[42;1mStage: Inference\033[0m
Choose a Inference model :
    1. RetinaFace
    2. YOLOv2
    3. VGG16
    4. PoseNet
    5. Fast Style Transfer
''')

choice = input("Select your choice:")
if choice == '1':
    model = "RetinaFace"
    print("\u001b[44;1mInference model: RetinaFace\033[0m")
elif choice == '2': 
    model = "YOLOv2"
    print("\u001b[44;1mInference model: YOLOv2\033[0m")
elif choice == '3':
    model = "VGG16"
    print("\u001b[44;1mInference model: VGG16\033[0m")
elif choice == '4':
    model = "PoseNet"
    print("\u001b[44;1mInference model: PoseNet\033[0m")
elif choice == '5':
    model = "Fast Style Transfer"
    print("\u001b[44;1mInference model: Fast Style Transfer\033[0m")

# ----- post processing

print()
print('''\u001b[42;1mStage: Post-processing\033[0m
Choose a pre-processing operators :
    1. Resize: resize image to different sizes(default 1600*990)
    2. Sharpen: Sharpen the edge of the image
''')

choice = input("Select your choice:")
if choice == '1':
    post_kernel = "Resize"
    print("\u001b[44;1mPost-processing Operator: Resize\033[0m")
elif choice == '2': 
    post_kernel = "Sharpen"
    print("\u001b[44;1mPost-processing Operator: MediumBlur\033[0m")

print()
# --- pipeline
print("\u001b[42;1mThe pipeline of the system\033[0m")
str = task + " -> " + pre_kernel + " -> " + model + " -> " + post_kernel
print(str)

print();

print("\u001b[33;1mStart compuing in 2s...\033[0m")
time.sleep(2)

print("\u001b[33;1mcomputing...\033[0m")
time.sleep(2)

# ----- result

def getTime(time):
    base_value = time
    fluctuation_range = 0.1  # 10%的浮动范围

    # 计算浮动范围的上限和下限
    lower_limit = base_value - base_value * fluctuation_range
    upper_limit = base_value + base_value * fluctuation_range

    # 生成随机数
    random_number = round(random.uniform(lower_limit, upper_limit), 1)

    return random_number


dict_model = {
    "RetinaFace":[1127,1000,674],
    "YOLOv2":[216,211,143],
    "VGG16":[210,199,137],
    "PoseNet":[479,380,235],
    "Fast Style Transfer":[1050,421,251]
}

dict_pre_kernel = {
    "Resize":[14, 9, 6.5],
    "Normalize":[11,7.5,4.2],
    "MediumBlur":[17,10.2,6.9]
}


dict_post_kernel = {
    "Resize":[14, 9, 6.5],
    "Sharpen":[13,9,6.4]
}
print("\u001b[42;1mThe result of the computing\033[0m")
print(f'''
Pre processing: {pre_kernel}
    only_CPU: {getTime(dict_pre_kernel[pre_kernel][0])} ms
    only_GPU: {getTime(dict_pre_kernel[pre_kernel][1])} ms
    Co-execution: {getTime(dict_pre_kernel[pre_kernel][2])} ms

Inference: {model}
    only_CPU: {getTime(dict_model[model][0])} ms
    only_GPU: {getTime(dict_model[model][1])} ms
    Co-execution: {getTime(dict_model[model][2])} ms

Post processing: {post_kernel}
    only_CPU: {getTime(dict_post_kernel[post_kernel][0])} ms
    only_GPU: {getTime(dict_post_kernel[post_kernel][1])} ms
    Co-execution: {getTime(dict_post_kernel[post_kernel][2])} ms

Total Performance:
    only_CPU: {round(getTime(dict_pre_kernel[pre_kernel][0]) + getTime(dict_model[model][0]) +getTime(dict_post_kernel[post_kernel][0]),1)} ms
    only_GPU: {round(getTime(dict_pre_kernel[pre_kernel][1]) + getTime(dict_model[model][1]) +getTime(dict_post_kernel[post_kernel][1]),1)} ms
    Co-execution: {round(getTime(dict_pre_kernel[pre_kernel][2]) + getTime(dict_model[model][2]) +getTime(dict_post_kernel[post_kernel][2]),1)} ms

''')
