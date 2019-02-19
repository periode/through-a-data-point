## TODO
- play a video on the raspberry pin (using `subprocess.POpen()` and `omxplayer`)
- write logic for one cycle
- - motors reset (how? manual setup? there should be an ssh connection possible to go and set it up)
- - 0. pick a video
- - 1. the video plays
- - 2. motors go up at a certain number of steps **step number is fixed for all motors** but there is the problem that sometimes the motors don't actually go through all the steps when they are too fast with the shift register... so we will need trial and error to figure out what is a safe number of steps
- - 3. once the numbers have gone up all these steps, we stop the video
- - 4. the motors go down the previous number of steps.
- - 5. go to step 1.

## MOTOR NOTES

for the motors pierre has:
- blue and yellow
- red and green

same coil: same side of the l293d
