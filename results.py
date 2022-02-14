import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import seaborn as sns

df = pd.DataFrame(data = {'base': base, 'contrast': contrast, 'brightness': brightness, 'sharpness': sharpness})
df.describe()

# scatter plot
plt.figure(figsize=(16, 10), dpi=200)

plt.scatter(base, [0]*len(base), c='r', alpha=0.3, label='base')
plt.plot([base.mean()], [0], 'ko', label='mean')

plt.scatter(contrast, [1]*len(base), c='g', alpha=0.3, label='contrast')
plt.plot([contrast.mean()], [1], 'ko')
plt.scatter(brightness, [2]*len(base), c='b', alpha=0.3, label='brightness')
plt.plot([brightness.mean()], [2], 'ko')
plt.scatter(sharpness, [3]*len(base), c='m', alpha=0.3, label='sharpness')
plt.plot([sharpness.mean()], [3], 'ko')

plt.xlabel('probability (percentage)')
plt.ylim((-1, 4))
plt.legend()
plt.show()

# violin plot
plt.figure(dpi=200)
sns.violinplot(data=df)
plt.show()

# average(probability) vs iteration 
# enhancement factor vs iteration

# update plot (contrast enhancement)
plt.figure(figsize=(16,6), dpi=200)

plt.subplot(121)
plt.plot(contrast, marker='o', color='r')
plt.xlabel('step')
plt.ylabel('probability sum')

plt.subplot(122)
plt.plot(c_step, marker='o', color='b')
plt.xlabel('step')
plt.ylim((0,2.5))
plt.ylabel('delta')

plt.suptitle('Contrast')
plt.show()

# update plot (brightness enhancement)
plt.figure(figsize=(16,6), dpi=200)

plt.subplot(121)
plt.plot(brightness, marker='o', color='r')
plt.xlabel('step')
plt.ylabel('probability sum')

plt.subplot(122)
plt.plot(b_step, marker='o', color='b')
plt.xlabel('step')
plt.ylim((0,2.5))
plt.ylabel('delta')

plt.suptitle('Brightness')
plt.show()

# update plot (sharpness enhancement)
plt.figure(figsize=(16,6), dpi=200)

plt.subplot(121)
plt.plot(sharpness, marker='o', color='r')
plt.xlabel('step')
plt.ylabel('probability sum')

plt.subplot(122)
plt.plot(s_step, marker='o', color='b')
plt.xlabel('step')
plt.ylim((0,2.5))
plt.ylabel('delta')

plt.suptitle('Sharpness')
plt.show()
