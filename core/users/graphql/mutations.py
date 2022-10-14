from email import message
import graphene

from django.conf import settings
from ..tasks import send_email


class SendEmailMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        message = graphene.String()
        email = graphene.String()
        subject = graphene.String()

    @classmethod
    def mutate(cls, root, message, email, subject):
        data = {
            "subject": "Message from admin",
            "apiKey": settings.API_KEY,
            "message": message,
            "email": email,
            "subject": subject,
        }
        send_email.apply_async([data], countdown=5)
        # Notice we return an instance of this mutation
        return SendEmailMutation(success=True)


class Mutation(graphene.ObjectType):
    send_email = SendEmailMutation.Field()
