from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
import requests

KV = '''
BoxLayout:
    orientation: 'vertical'
    spacing: '20dp'
    padding: '20dp'
    
    MDTextField:
        id: review_input
        hint_text: 'Skriv inn tekst her'
        multiline: True
    
    MDRaisedButton:
        text: 'Analyser tekst'
        size_hint_y: None
        height: '48dp'
        on_release: app.analyze_review()
    
    MDTextField:
        id: result_label
        hint_text: 'SentimentAI resultat'
        multiline: True
'''

class MovieReviewApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def analyze_review(self):
        review_text = self.root.ids.review_input.text
        if review_text:
            try:
                # Send a POST request to the Flask API
                response = requests.post('http://127.0.0.1:5000/analyze', json={'text': review_text})
                response_data = response.json()

                # Update the UI with the sentiment analysis result
                result_text = f"Sentiment: {response_data['sentiment']} " \
                              f"Confidence: {response_data['confidence']:.2f}"
                self.root.ids.result_label.text = result_text

            except requests.RequestException as e:
                print(f"Error in Kivy App: {e}")
                self.root.ids.result_label.text = "Error: Unable to connect to the server"
            except Exception as e:
                print(f"Unhandled Error in Kivy App: {e}")

if __name__ == '__main__':
    MovieReviewApp().run()
