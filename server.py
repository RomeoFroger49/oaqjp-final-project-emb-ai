''' 
    This function initiates the rendering of the main application
    page over the Flask channel
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import predict_emotion

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using predict_emotion()
        function. The output returned shows the different emotions
        detected along with their corresponding scores and the
        dominant emotion.
    '''

    # Get the text to be analyzed from the HTML interface
    text_to_analyse = request.args.get('textToAnalyze')

    # Get the response from the emotion detection model
    response = predict_emotion(text_to_analyse)

    # Return a formatted string with the different emotions and scores and dominant emotion
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominate_emotion']}."
    )



@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
