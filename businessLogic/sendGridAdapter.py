from emailAdapter import *
import sendgrid

class sendGridAdapter (emailAdapter):


	def __init__(self, apiKey):
		self.apiKey = apiKey

	def sendEmail(self,data):
		client = sendgrid.SendGridClient(self.apiKey)
		message = sendgrid.Mail()

		message.add_to(data['to'])
		message.set_from(data['from'])
		message.set_subject(data['subject'])
		message.set_html(data['text'])
		print client.send(message)

		
