from database1 import SessionLocal, MoodResource, MoodActivity

db = SessionLocal()

# Insert Mood-Based Resources (2 YouTube videos, 2 Articles, 2 Podcasts per mood)
resources = [
    # Happy
    MoodResource(mood="happy", type="youtube", title="The Science of Happiness", url="https://www.youtube.com/watch?v=fjZ_JcTp9I0"),
    MoodResource(mood="happy", type="youtube", title="10-Minute Guided Happiness Meditation", url="https://www.youtube.com/watch?v=R9z2ELaBVJY"),
    MoodResource(mood="happy", type="article", title="How to Stay Happy Every Day", url="https://www.psychologytoday.com/us/blog/the-science-happiness"),
    MoodResource(mood="happy", type="article", title="10 Simple Ways to Boost Happiness", url="https://www.healthline.com/nutrition/how-to-be-happy"),
    MoodResource(mood="happy", type="podcast", title="The Happiness Lab", url="https://www.happinesslab.fm/"),
    MoodResource(mood="happy", type="podcast", title="The Science of Happiness", url="https://greatergood.berkeley.edu/podcasts"),

    # Sad
    MoodResource(mood="sad", type="youtube", title="How to Cope with Sadness", url="https://www.youtube.com/watch?v=2FLK2Ht1h9s"),
    MoodResource(mood="sad", type="youtube", title="Motivational Video for Tough Times", url="https://www.youtube.com/watch?v=mgmVOuLgFB0"),
    MoodResource(mood="sad", type="article", title="Dealing with Sadness: Tips from Experts", url="https://www.verywellmind.com/dealing-with-sadness"),
    MoodResource(mood="sad", type="article", title="Why Do We Feel Sad? The Science Behind It", url="https://www.psychologytoday.com/us/basics/sadness"),
    MoodResource(mood="sad", type="podcast", title="Therapy Chat Podcast", url="https://www.therapychatpodcast.com/"),
    MoodResource(mood="sad", type="podcast", title="The Mental Illness Happy Hour", url="https://mentalpod.com/"),

    # Anxious
    MoodResource(mood="anxious", type="youtube", title="10-Minute Guided Anxiety Relief Meditation", url="https://www.youtube.com/watch?v=4pLUleLdwY4"),
    MoodResource(mood="anxious", type="youtube", title="How to Overcome Anxiety Naturally", url="https://www.youtube.com/watch?v=WWloIAQpMcQ"),
    MoodResource(mood="anxious", type="article", title="5 Ways to Reduce Anxiety", url="https://www.anxietycanada.com/articles/how-to-reduce-anxiety/"),
    MoodResource(mood="anxious", type="article", title="Understanding Anxiety Disorders", url="https://www.nimh.nih.gov/health/topics/anxiety-disorders"),
    MoodResource(mood="anxious", type="podcast", title="The Anxiety Coaches Podcast", url="https://www.theanxietycoachespodcast.com/"),
    MoodResource(mood="anxious", type="podcast", title="UnF*ck Your Brain (Anxiety & Mindset)", url="https://unfuckyourbrain.com/podcast/"),

    # Stressed
    MoodResource(mood="stressed", type="youtube", title="Stress Relief Meditation", url="https://www.youtube.com/watch?v=oVzTnS_IONU"),
    MoodResource(mood="stressed", type="youtube", title="How to Reduce Stress Quickly", url="https://www.youtube.com/watch?v=Wemm-i6XHr8"),
    MoodResource(mood="stressed", type="article", title="10 Ways to Reduce Stress", url="https://www.helpguide.org/articles/stress/stress-relief.htm"),
    MoodResource(mood="stressed", type="article", title="How to Manage Workplace Stress", url="https://www.psychologytoday.com/us/workplace-stress"),
    MoodResource(mood="stressed", type="podcast", title="The Mindful Minute", url="https://themindfulminute.com/"),
    MoodResource(mood="stressed", type="podcast", title="The Daily Meditation Podcast", url="https://www.sipandom.com/podcast"),

    # Angry
    MoodResource(mood="angry", type="youtube", title="How to Control Anger", url="https://www.youtube.com/watch?v=H0nwM7O8gEU"),
    MoodResource(mood="angry", type="youtube", title="Guided Meditation for Letting Go of Anger", url="https://www.youtube.com/watch?v=BZnOwAdXnYU"),
    MoodResource(mood="angry", type="article", title="Managing Anger Effectively", url="https://www.apa.org/topics/anger/control"),
    MoodResource(mood="angry", type="article", title="Why Do We Get Angry? The Psychology Behind It", url="https://www.psychologytoday.com/us/anger-issues"),
    MoodResource(mood="angry", type="podcast", title="The Anger Management Podcast", url="https://www.angermanagementpodcast.com/"),
    MoodResource(mood="angry", type="podcast", title="Unlocking Us (Emotional Control)", url="https://brenebrown.com/podcast/introducing-unlocking-us/"),

    #calm
    MoodResource(mood="calm", type="youtube", title="Relaxing Nature Sounds", url="https://www.youtube.com/watch?v=1ZYbU82GVz4"),
    MoodResource(mood="calm", type="youtube", title="10-Minute Guided Mindfulness Meditation", url="https://www.youtube.com/watch?v=U9YKY7fdwyg"),
    MoodResource(mood="calm", type="article", title="How to Cultivate Inner Peace", url="https://www.mindful.org/10-ways-to-feel-more-peaceful/"),
    MoodResource(mood="calm", type="article", title="The Science of Calm", url="https://www.npr.org/sections/health-shots/2021/calm-brain"),
    MoodResource(mood="calm", type="podcast", title="The Calm Podcast", url="https://www.calm.com/podcast"),
    MoodResource(mood="calm", type="podcast", title="Sleepy (Calming Bedtime Stories)", url="https://www.sleepypodcast.com/"),

    # Euphoric
    MoodResource(mood="euphoric", type="youtube", title="The Neuroscience of Euphoria", url="https://www.youtube.com/watch?v=g6tZepLs7v4"),
    MoodResource(mood="euphoric", type="youtube", title="Feel-Good Music Mix", url="https://www.youtube.com/watch?v=JmC2igVh0nE"),
    MoodResource(mood="euphoric", type="article", title="What Causes Euphoria?", url="https://www.scientificamerican.com/article/what-causes-euphoria/"),
    MoodResource(mood="euphoric", type="article", title="Harnessing Positive Emotions", url="https://positivepsychology.com/positive-emotions/"),
    MoodResource(mood="euphoric", type="podcast", title="Feel Better, Live More", url="https://drchatterjee.com/podcast/"),
    MoodResource(mood="euphoric", type="podcast", title="Happier with Gretchen Rubin", url="https://gretchenrubin.com/podcasts/"),

    # Disappointed
    MoodResource(mood="disappointed", type="youtube", title="How to Deal with Disappointment", url="https://www.youtube.com/watch?v=Bb3v5wR-Kng"),
    MoodResource(mood="disappointed", type="youtube", title="The Art of Letting Go", url="https://www.youtube.com/watch?v=Tfn6xV5g25U"),
    MoodResource(mood="disappointed", type="article", title="Coping with Disappointment", url="https://www.verywellmind.com/how-to-cope-with-disappointment-5205072"),
    MoodResource(mood="disappointed", type="article", title="5 Ways to Manage Disappointment", url="https://www.psychologytoday.com/us/blog/how-cope-disappointment"),
    MoodResource(mood="disappointed", type="podcast", title="On Purpose with Jay Shetty", url="https://jayshetty.me/podcast/"),
    MoodResource(mood="disappointed", type="podcast", title="The Mindset Mentor", url="https://robdial.com/podcast/"),

    # Bored
    MoodResource(mood="bored", type="youtube", title="How to Overcome Boredom", url="https://www.youtube.com/watch?v=4fYwKzQ2D1A"),
    MoodResource(mood="bored", type="youtube", title="Try These Fun Activities When Bored", url="https://www.youtube.com/watch?v=aAzzrAO0hsk"),
    MoodResource(mood="bored", type="article", title="10 Creative Ways to Kill Boredom", url="https://www.lifehack.org/articles/productivity/10-ways-overcome-boredom.html"),
    MoodResource(mood="bored", type="article", title="The Psychology of Boredom", url="https://www.psychologytoday.com/us/boredom"),
    MoodResource(mood="bored", type="podcast", title="The Infinite Monkey Cage", url="https://www.bbc.co.uk/programmes/b00snr0w"),
    MoodResource(mood="bored", type="podcast", title="Stuff You Should Know", url="https://www.iheart.com/podcast/105-stuff-you-should-know-26940277/"),

]

db.add_all(resources)
db.commit()

# Insert Mood-Based Activities (2 per mood)
activities = [
    MoodActivity(mood="happy", activity="Practice gratitude journaling"),
    MoodActivity(mood="happy", activity="Listen to uplifting music"),
    
    MoodActivity(mood="sad", activity="Write in a journal about your feelings"),
    MoodActivity(mood="sad", activity="Watch a comforting movie"),
    
    MoodActivity(mood="anxious", activity="Practice deep breathing exercises"),
    MoodActivity(mood="anxious", activity="Engage in progressive muscle relaxation"),
    
    MoodActivity(mood="stressed", activity="Take a short walk in nature"),
    MoodActivity(mood="stressed", activity="Listen to calming instrumental music"),
    
    MoodActivity(mood="angry", activity="Try physical exercise (running, punching bag)"),
    MoodActivity(mood="angry", activity="Practice controlled breathing techniques"),
    
    MoodActivity(mood="calm", activity="Listen to ocean or rain sounds"),
    MoodActivity(mood="calm", activity="Drink herbal tea while reading"),
    
    MoodActivity(mood="euphoric", activity="Express yourself through dance or music"),
    MoodActivity(mood="euphoric", activity="Share your happiness with loved ones"),
    
    MoodActivity(mood="disappointed", activity="Write down lessons learned"),
    MoodActivity(mood="disappointed", activity="Focus on personal growth"),
    
    MoodActivity(mood="bored", activity="Try learning a new hobby"),
    MoodActivity(mood="bored", activity="Watch an interesting documentary"),
]

db.add_all(activities)
db.commit()
db.close()
