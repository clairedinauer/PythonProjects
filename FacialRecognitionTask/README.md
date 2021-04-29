#  Face Manipulation Recognition Task
 
Experimenters: Claire Dinauer and Nikka Mel Ruelos

Author of this Page: Claire Dinauer

Date: December 11, 2020
 
## The Problem

With the rapid expansion of social media platforms over the past decade, the use of face distortion and filters for users’ entertainment has exploded. Many of these filters introduced by social media platforms, most notably Instagram and Snapchat, warp users’ face or certain facial features beyond recognition. While these filters are fun for entertainment purposes, questions arise regarding to what extent they affect how well we can recognize individuals. 

Previous literature suggests that people can to recognize and reconstruct faces to a respectable degree when viewing them with occlusions, in different lighting, from different angles, when slightly blurred, and in different contexts (Lu & Liu, 2008; Lee et al., 2005; Lam & Yan, 1998; Harmon, 1973). This brings us to ask, to what extent is recognition impaired when the image of a face distorted? And how may the amount of distortion impact later recognition? Are we more likely to recognize the distorted face or a more “normal” face?

## Our Interests

Given the literature and culture surrounding this topic, we are interested in exploring how well people are able to recognize faces after seeing a largely distorted version of them, and whether people are better able to recognize the faces when presented with the same or a lesser amount of distortion. We are also interested in investigating whether asking participants to recall an image versus a face has an effect on recognition abilities. To do this, we created an “old-new” recognition task, in which recognition required individuals to distinguish “old” (previously presented) faces from “new” (newly presented) faces with varying degrees of distortion. All faces presented in the learning task, which would be considered old during the recognition task, were largely distorted by stretching the images both vertically and horizontally to create a “wave” effect, similar to that of a distortion filter offered by Snapchat. 

## Participants

The participants were 11 undergraduate college students (nine men, two women, age range: 20-22 years) at the University of California, Los Angeles. The participants participated for course credit in an upper-division psychology course. All participants were fluent in English.

## Design

The experiment utilized a two-way within-subjects design to investigate how manipulating the amount of image distortion and instruction types affect one’s ability to recognize faces in an old/new recognition task. The amount of distortion was operationalized as the degree to which images were warped to make faces less recognizable, while instruction type was operationalized as the wording of the set of instructions given before each learning phase. The amount of distortion was manipulated across two levels: large distortion and small distortion. In the large distortion condition, faces were distorted with a wave stretch frequency of seven (i.e to the seventh degree); in the small distortion condition, faces were distorted with a wave stretch frequency of three (i.e. to the third degree), meaning that the amount of distortion was mild and the faces more closely resembled normal human faces. The type of instructions was also manipulated across two levels: image recognition and face recognition. In the image recognition condition, participants were instructed to remember each image, as they would later be tested on their image recognition abilities. In the face recognition condition, participants were instructed to remember each face, as they would be tested on their face recognition abilities. The dependent variable under investigation was the participants’ performance statistics, specifically pertaining to their percentage of correct responses, d' (sensitivity), and logβ (bias).

Each image was presented in a randomized order. Instruction type was also randomized, in which subjects either received the face instructions (FI) or image instructions (II) first. The amount of distortion applied to each image in the recognition portion of the task was randomized, in which half of the images were largely distorted (LD) and the other half were slightly distorted (SD).

## Materials and Apparatus

Stimuli for the experimental trials consisted of 120 frontal-view professional headshot photos, with images of 60 women and 60 men who varied in terms of appearances, ages, and racial backgrounds. All images were set to grayscale colors to avoid ceiling effects. The images were cropped into squares with consistent dimensions to ensure that faces were in the center of the screen. Sixty of the 120 images were randomly assigned to be stimuli presented during one of the two learning trials, which would be the old images in the old/new task. The remaining sixty images were assigned to be the new images, or the noise, to be presented during the recognition trials of the old/new task. The code for the experiment was written in Python and used PsychoPy for core, visual, GUI, event, and data functions.

## Procedure

Participants were instructed to run the experimental file through Python. Participants were first prompted to enter their subject information, such as initials and age. Before the experiment began, the 120 face photos were randomly assigned and equally divided to be a stimulus or noise face. Next, one of the two sets of instructions was shown to the participant, in which instruction type was counterbalanced by randomly assigning subjects to view the face instructions or image instructions first. After the instructions were shown, participants were given 3 seconds to memorize each of the 30 faces in the set. All of the stimuli faces were largely distorted in the learning portion of the task. Participants were then told to identify the faces based on whether they saw the face in the previous set (“old”) or did not see the face (“new”). The participant would then see the 30 stimuli headshot photos (old faces) and 30 noise headshot photos (new faces) in a randomized order, in which 15 stimuli and 15 noise images were randomly assigned to the large distortion condition and the remaining 15 stimuli and 15 noise images were assigned to the small distortion condition. Figure 1 (below) offers an example of how images were distorted for the learning and recognition tasks. The faces were presented one at a time, each for 700 milliseconds. After each face presentation, the participant was prompted to press ‘1’ on their keyboard to indicate that the face was old or press ‘2’ to indicate that the face was new. This procedure was repeated for the second set of instructions until participants had viewed all 120 headshot photos. To avoid confusion or interference, headshot photos were not repeated across conditions.

