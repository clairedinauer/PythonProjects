"""
Dinauer_Ruelos.py
Claire Dinauer and Nikka Ruelos

- See README.txt for information about this task!
- Claire's Email: cdinauer@g.ucla.edu
- Nikka's Email: nruelos@g.ucla.edu

"""

from psychopy import core, visual, gui, data, event
import numpy
import random
from PIL import Image, ImageOps  # for greyscale and flipping of images
import pandas as pd


"""
Experiment Creation:

Variables to be determined:
-window size [length, width]
-learning_length : of each face during the learning trial (set between 2 to 5 secs)
-test_length : of each face during each trial (set between .25 to .5 secs)
-faces_total : change to 120 for actual experiment
"""
wind_w = 850
wind_h = 450
wind_ratio = wind_h/wind_w

learning_length = 1
# in seconds, how long will the observer have to memorize a faces

test_length = 2
# in seconds, how long will the signal and noise faces will be displayed in a trial

faces_total = 120  # number of total faces
t_half = faces_total//2  # number of signal_faces

# initializing the random number generator
random.seed()
seed = random.random() * 186
random.seed(seed)

timer = core.Clock()
# initializing the timer

"""
Asking for Participant Info
"""
dialog_box = gui.Dlg(title="Participant Info")
dialog_box.addText('Please answer the questions below')
dialog_box.addField('Initials:')
dialog_box.addField('Age:')
dialog_box.addField('Gender (M/F/NB):')
dialog_box.addField('Major:')
dialog_box.addField('Ethnicity:')
dialog_box.addField('Year in School:', choices=[
                    "Freshman", "Sophomore", "Junior", "Senior", "5th year +"])
dialog_box.addField('On a Scale of 1 to 5, how good do you think you are at recognizing faces?',
                    choices=["1 (Not Good At All)", "2", "3", "4", "5 (Very Good)"])
dialog_box.addField('On a Scale of 1 to 5, how familiar are you with photo-filters\n (For example, face distortions on Snapchat or Photo Booth)?',
                    choices=["1 (Not At All)", "2", "3", "4", "5 (Very Familiar)"])
dialog_box.addField('Random Seed', seed, enabled=False)
participant_data = dialog_box.show()  # show dialog and wait for OK or Cancel


# cropping the image
def crop_square(pil_img):
    # note: takes in PIL.Image, not visual.ImageStim
    img_width, img_height = pil_img.size
    crop_size = min(img_width, img_height)
    return pil_img.crop(((img_width - crop_size) // 2,
                         (img_height - crop_size) // 2,
                         (img_width + crop_size) // 2,
                         (img_height + crop_size) // 2))


# distorting the image
def wave_distort(normal_image, amount):
    # note: takes in PIL.Image, not visual.ImageStim
    normal_array = numpy.asarray(normal_image)

    # create array of image size
    distortion_array = numpy.zeros((normal_array.shape[0], normal_array.shape[1]))
    width = normal_array.shape[0]
    height = normal_array.shape[1]

    """
    If you wish to change distortion amount, change number f
    """
    # frequency -stretch of wave
    f = 3 if amount == 'small' else 7

    # wave(x) = Amplitude * numpy.sin( frequency * x / (width or height to make things smooth))

    def hori_wave(x):  # pixels are moved up or down
        return width/15 * numpy.sin(f * x / height)

    for i in range(normal_array.shape[1]):
        distortion_array[:, i] = numpy.roll(normal_array[:, i], int(hori_wave(i)))

    def vert_wave(x):  # pixels are moved left or right
        return height/15 * numpy.sin(f * x / width)

    for i in range(distortion_array.shape[0]):
        distortion_array[i, :] = numpy.roll(distortion_array[i, :], int(vert_wave(i)))

    distorted_image = Image.fromarray(distortion_array)

    return distorted_image


"""
Opening the Window
"""
win = visual.Window([wind_w, wind_h], multiSample=True)
win.flip()

""" DICTIONARIES OF FACES: CREATION """
# Faces
large_distortions = {}
small_distortions = {}
signal_nums = []
noise_nums = []

for num in range(faces_total):
    image_name = str('face' + str(num) + '.jpg')
    image = Image.open('Faces/' + image_name)
    grey_face = image.convert('L')
    square_face = crop_square(grey_face)

    large_distort = wave_distort(square_face, 'large')
    small_distort = wave_distort(square_face, 'small')

    if random.random() > .5:
        large_distort = ImageOps.mirror(large_distort)
        small_distort = ImageOps.mirror(small_distort)

    # creation of dictionary of large distorted faces accessible by [number_key]
    large_distortions[num] = visual.ImageStim(win, image=large_distort, size=[wind_ratio*1.5, 1.5])

    # creation of dictionary of small distorted faces accessible by [number_key]
    small_distortions[num] = visual.ImageStim(win, image=small_distort, size=[wind_ratio*1.5, 1.5])

    # determining signal and noise faces
    if (random.random() < .5 and len(signal_nums) < t_half) or len(noise_nums) >= t_half:
        signal_nums.append(num)
    else:
        noise_nums.append(num)


"""
Splitting Experiment into 2 sections
"""

random.shuffle(signal_nums)
random.shuffle(noise_nums)

signals_A = signal_nums[:len(signal_nums)//2]
signals_B = signal_nums[len(signal_nums)//2:]
# print(signals_A)
# print(signals_B)
signals_list = [signals_A, signals_B]
# print(signals_list)
# print(signals_list[0])
# print(signals_list[0][3])


noises_A = noise_nums[:len(noise_nums)//2]
noises_B = noise_nums[len(noise_nums)//2:]
noises_list = [noises_A, noises_B]

face_number = []  # for recording purposes
trial_conditions = []  # signal (1) or noise (2), 30 total, compare to responses
trial_distortions = []  # large or small, 30 total
responses = []
response_time = []  # tracking of response time per trial

instruction_focus = []  # what the subjects are being asked to recall
instruction_order = [1, 2]  # the order in which the instructions are presented
random.shuffle(instruction_order)  # randomizing the order of the instructions
# labels for type of instructions given:
instruction_face = ['face']*60
instruction_image = ['image']*60

# initializing the instructions for learning and testing portions
instructionsLearning = visual.TextStim(win, text='')
instructionsLearning.autoDraw = False
instructionsTesting = visual.TextStim(win, text='')
instructionsTesting.autoDraw = False

generalInstructions = visual.TextStim(win, text='Press 1(old) or 2(new)')
generalInstructions.autoDraw = False

"""
At this point, the experiment splits into sessions 1 and 2 using a for loop
"""

for section in range(2):
    """
    Learning Phase:

    """
    if instruction_order[section] == 1:
        instruction_focus.extend(instruction_face)
        instructionsLearning.text = (
            'In this phase, you will have %s seconds to remember each face. You will later be tested on your ability to recall each face.' % learning_length)
        instructionsTesting.text = ("In this phase, you will see a face." +
                                    "\n The face may or may not have been from the learning phase." +
                                    "\n Press 1 if you saw the face in the learning phase. Press 2 if not.")
    elif instruction_order[section] == 2:
        instruction_focus.extend(instruction_image)
        instructionsLearning.text = (
            'In this phase, you will have %s seconds to remember each image. You will later be tested on your ability to recall each image.' % learning_length)
        instructionsTesting.text = ("In this phase, you will see an image." +
                                    "\n The image may or may not have been from the learning phase." +
                                    "\n Press 1 if you saw the image in the learning phase. Press 2 if not.")

    instructionsLearning.draw()

    win.flip()
    core.wait(6)

    random.shuffle(signals_list[section])
    # print(signals_list[section])

    for num in signals_list[section]:
        large_distortions[num].draw()
        win.flip()
        core.wait(learning_length)

        win.flip()
        core.wait(.3)

    """
    Testing Phase:

    """

    instructionsTesting.draw()
    win.flip()
    core.wait(10)

    random.shuffle(signals_list[section])
    random.shuffle(noises_list[section])

    signals_done = 0
    noises_done = 0

    S_small_dist_done = 0
    N_small_dist_done = 0
    S_large_dist_done = 0
    N_large_dist_done = 0

    for i in range(t_half):
        # determining if face is signal or noise for test
        if (random.random() < .5 and signals_done < len(signals_list[section])) or noises_done >= len(noises_list[section]):
            # signal is shown
            trial_conditions.append('1')
            face_to_show = signals_list[section][signals_done]
            face_number.append(face_to_show)
            signals_done += 1
            # determining if face is distorted or not
            if (random.random() < .5 and S_small_dist_done < (t_half//4)) or S_large_dist_done >= (t_half//4):
                # signal is shown
                trial_distortions.append('small')
                small_distortions[face_to_show].draw()
                S_small_dist_done += 1
            else:
                # noise is shown
                trial_distortions.append('large')
                large_distortions[face_to_show].draw()
                S_large_dist_done += 1
        else:
            # noise is shown
            trial_conditions.append('2')
            face_to_show = noises_list[section][noises_done]
            face_number.append(face_to_show)
            noises_done += 1
            if (random.random() < .5 and N_small_dist_done < (t_half//4)) or N_large_dist_done >= (t_half//4):
                # signal is shown
                trial_distortions.append('small')
                small_distortions[face_to_show].draw()
                N_small_dist_done += 1
            else:
                # noise is shown
                trial_distortions.append('large')
                large_distortions[face_to_show].draw()
                N_large_dist_done += 1

        win.flip()
        core.wait(2)

        # Gather Response
        generalInstructions.draw()
        win.flip()

        key_press = None
        timer.reset()  # setting time to be 0
        while key_press == None:
            key_press = event.waitKeys(keyList=['1', '2', 'q', 'escape'])
            for this_key in key_press:
                respTime = timer.getTime()  # getting response time
                if this_key in ['q', 'escape']:
                    core.quit()  # end experiment
                else:
                    responses.append(int(this_key))
                    response_time.append(respTime)

        win.flip()
        core.wait(.2)

        event.clearEvents()


# DATA RECORD

trial = [number for number in range(1, faces_total+1)]

data = pd.DataFrame(list(zip(trial, face_number, trial_distortions, trial_conditions, responses, instruction_focus, response_time)), columns=[
                    'Trial #', 'Face #', 'Distortion', 'Condition', 'Response', 'Instructions', 'Response Time'])

data.to_csv('subjects_data.csv', index=False)

info = pd.DataFrame(participant_data, columns=["Participant Info"])
info.to_csv('participant_info.csv', index=False)


# CLOSE OUT THE EXPERIMENT

generalInstructions.text = "This was the end of the experiment. Please send 2 .csv files that were generated to the researchers. Press 'q' to end the experiment."

generalInstructions.draw()
win.flip()

key_press = None
while key_press == None:
    key_press = event.waitKeys(keyList=['q', 'escape'])
    for this_key in key_press:
        if this_key in ['q', 'escape']:
            core.quit()
