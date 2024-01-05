# schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import Utilisateur, Conversation, Message, PieceJointe, DestinataireMessage, CopieCarbone, MessageEnvoye, MessageRecu, Brouillon, Corbeille

class UtilisateurType(DjangoObjectType):
    class Meta:
        model = Utilisateur

class ConversationType(DjangoObjectType):
    class Meta:
        model = Conversation

class MessageType(DjangoObjectType):
    class Meta:
        model = Message

class PieceJointeType(DjangoObjectType):
    class Meta:
        model = PieceJointe

class DestinataireMessageType(DjangoObjectType):
    class Meta:
        model = DestinataireMessage

class CopieCarboneType(DjangoObjectType):
    class Meta:
        model = CopieCarbone

class MessageEnvoyeType(DjangoObjectType):
    class Meta:
        model = MessageEnvoye

class MessageRecuType(DjangoObjectType):
    class Meta:
        model = MessageRecu

class BrouillonType(DjangoObjectType):
    class Meta:
        model = Brouillon

class CorbeilleType(DjangoObjectType):
    class Meta:
        model = Corbeille

class UtilisateurInput(graphene.InputObjectType):
    nom = graphene.String()
    email = graphene.String()
    mot_de_passe = graphene.String()

# Define similar input types for other models
class CreateUtilisateur(graphene.Mutation):
    utilisateur = graphene.Field(UtilisateurType)

    class Arguments:
        input = UtilisateurInput(required=True)

    def mutate(self, info, input):
        utilisateur = Utilisateur(**input)
        utilisateur.save()
        return CreateUtilisateur(utilisateur=utilisateur)

class UpdateUtilisateur(graphene.Mutation):
    utilisateur = graphene.Field(UtilisateurType)

    class Arguments:
        id = graphene.ID(required=True)
        input = UtilisateurInput(required=True)

    def mutate(self, info, id, input):
        utilisateur = Utilisateur.objects.get(pk=id)
        for key, value in input.items():
            setattr(utilisateur, key, value)
        utilisateur.save()
        return UpdateUtilisateur(utilisateur=utilisateur)

class DeleteUtilisateur(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        utilisateur = Utilisateur.objects.get(pk=id)
        utilisateur.delete()
        return DeleteUtilisateur(success=True)

# ______________________
class ConversationInput(graphene.InputObjectType):
    expediteur_id = graphene.ID()

class CreateConversation(graphene.Mutation):
    conversation = graphene.Field(ConversationType)

    class Arguments:
        input = ConversationInput(required=True)

    def mutate(self, info, input):
        conversation = Conversation(**input)
        conversation.save()
        return CreateConversation(conversation=conversation)

class UpdateConversation(graphene.Mutation):
    conversation = graphene.Field(ConversationType)

    class Arguments:
        id = graphene.ID(required=True)
        input = ConversationInput(required=True)

    def mutate(self, info, id, input):
        conversation = Conversation.objects.get(pk=id)
        for key, value in input.items():
            setattr(conversation, key, value)
        conversation.save()
        return UpdateConversation(conversation=conversation)

class DeleteConversation(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        conversation = Conversation.objects.get(pk=id)
        conversation.delete()
        return DeleteConversation(success=True)

# _________________________________
class MessageInput(graphene.InputObjectType):
    conversation_id = graphene.ID()
    expediteur_id = graphene.ID()

class CreateMessage(graphene.Mutation):
    message = graphene.Field(MessageType)

    class Arguments:
        input = MessageInput(required=True)

    def mutate(self, info, input):
        message = Message(**input)
        message.save()
        return CreateMessage(message=message)

class UpdateMessage(graphene.Mutation):
    message = graphene.Field(MessageType)

    class Arguments:
        id = graphene.ID(required=True)
        input = MessageInput(required=True)

    def mutate(self, info, id, input):
        message = Message.objects.get(pk=id)
        for key, value in input.items():
            setattr(message, key, value)
        message.save()
        return UpdateMessage(message=message)

class DeleteMessage(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        message = Message.objects.get(pk=id)
        message.delete()
        return DeleteMessage(success=True)
# ______________________
# PieceJointe

class PieceJointeInput(graphene.InputObjectType):
    expediteur_id = graphene.ID()
    message_id = graphene.ID()

class CreatePieceJointe(graphene.Mutation):
    piece_jointe = graphene.Field(PieceJointeType)

    class Arguments:
        input = PieceJointeInput(required=True)

    def mutate(self, info, input):
        piece_jointe = PieceJointe(**input)
        piece_jointe.save()
        return CreatePieceJointe(piece_jointe=piece_jointe)

class UpdatePieceJointe(graphene.Mutation):
    piece_jointe = graphene.Field(PieceJointeType)

    class Arguments:
        id = graphene.ID(required=True)
        input = PieceJointeInput(required=True)

    def mutate(self, info, id, input):
        piece_jointe = PieceJointe.objects.get(pk=id)
        for key, value in input.items():
            setattr(piece_jointe, key, value)
        piece_jointe.save()
        return UpdatePieceJointe(piece_jointe=piece_jointe)

class DeletePieceJointe(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        piece_jointe = PieceJointe.objects.get(pk=id)
        piece_jointe.delete()
        return DeletePieceJointe(success=True)

# ______________________
# DestinataireMessage

class DestinataireMessageInput(graphene.InputObjectType):
    expediteur_id = graphene.ID()
    message_id = graphene.ID()
    destinataire_id = graphene.ID()

class CreateDestinataireMessage(graphene.Mutation):
    destinataire_message = graphene.Field(DestinataireMessageType)

    class Arguments:
        input = DestinataireMessageInput(required=True)

    def mutate(self, info, input):
        destinataire_message = DestinataireMessage(**input)
        destinataire_message.save()
        return CreateDestinataireMessage(destinataire_message=destinataire_message)

class UpdateDestinataireMessage(graphene.Mutation):
    destinataire_message = graphene.Field(DestinataireMessageType)

    class Arguments:
        id = graphene.ID(required=True)
        input = DestinataireMessageInput(required=True)

    def mutate(self, info, id, input):
        destinataire_message = DestinataireMessage.objects.get(pk=id)
        for key, value in input.items():
            setattr(destinataire_message, key, value)
        destinataire_message.save()
        return UpdateDestinataireMessage(destinataire_message=destinataire_message)

class DeleteDestinataireMessage(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        destinataire_message = DestinataireMessage.objects.get(pk=id)
        destinataire_message.delete()
        return DeleteDestinataireMessage(success=True)
# ______________________
# CopieCarbone

class CopieCarboneInput(graphene.InputObjectType):
    expediteur_id = graphene.ID()
    message_envoye_id = graphene.ID()
    utilisateur_cc_id = graphene.ID()

class CreateCopieCarbone(graphene.Mutation):
    copie_carbone = graphene.Field(CopieCarboneType)

    class Arguments:
        input = CopieCarboneInput(required=True)

    def mutate(self, info, input):
        copie_carbone = CopieCarbone(**input)
        copie_carbone.save()
        return CreateCopieCarbone(copie_carbone=copie_carbone)

class UpdateCopieCarbone(graphene.Mutation):
    copie_carbone = graphene.Field(CopieCarboneType)

    class Arguments:
        id = graphene.ID(required=True)
        input = CopieCarboneInput(required=True)

    def mutate(self, info, id, input):
        copie_carbone = CopieCarbone.objects.get(pk=id)
        for key, value in input.items():
            setattr(copie_carbone, key, value)
        copie_carbone.save()
        return UpdateCopieCarbone(copie_carbone=copie_carbone)

class DeleteCopieCarbone(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        copie_carbone = CopieCarbone.objects.get(pk=id)
        copie_carbone.delete()
        return DeleteCopieCarbone(success=True)
# ______________________
# MessageEnvoye

class MessageEnvoyeInput(graphene.InputObjectType):
    expediteur_id = graphene.ID()
    destinataire_id = graphene.ID()

class CreateMessageEnvoye(graphene.Mutation):
    message_envoye = graphene.Field(MessageEnvoyeType)

    class Arguments:
        input = MessageEnvoyeInput(required=True)

    def mutate(self, info, input):
        message_envoye = MessageEnvoye(**input)
        message_envoye.save()
        return CreateMessageEnvoye(message_envoye=message_envoye)

class UpdateMessageEnvoye(graphene.Mutation):
    message_envoye = graphene.Field(MessageEnvoyeType)

    class Arguments:
        id = graphene.ID(required=True)
        input = MessageEnvoyeInput(required=True)

    def mutate(self, info, id, input):
        message_envoye = MessageEnvoye.objects.get(pk=id)
        for key, value in input.items():
            setattr(message_envoye, key, value)
        message_envoye.save()
        return UpdateMessageEnvoye(message_envoye=message_envoye)

class DeleteMessageEnvoye(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        message_envoye = MessageEnvoye.objects.get(pk=id)
        message_envoye.delete()
        return DeleteMessageEnvoye(success=True)
# ______________________
# MessageRecu

class MessageRecuInput(graphene.InputObjectType):
    expediteur_id = graphene.ID()
    destinataire_id = graphene.ID()

class CreateMessageRecu(graphene.Mutation):
    message_recu = graphene.Field(MessageRecuType)

    class Arguments:
        input = MessageRecuInput(required=True)

    def mutate(self, info, input):
        message_recu = MessageRecu(**input)
        message_recu.save()
        return CreateMessageRecu(message_recu=message_recu)

class UpdateMessageRecu(graphene.Mutation):
    message_recu = graphene.Field(MessageRecuType)

    class Arguments:
        id = graphene.ID(required=True)
        input = MessageRecuInput(required=True)

    def mutate(self, info, id, input):
        message_recu = MessageRecu.objects.get(pk=id)
        for key, value in input.items():
            setattr(message_recu, key, value)
        message_recu.save()
        return UpdateMessageRecu(message_recu=message_recu)

class DeleteMessageRecu(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        message_recu = MessageRecu.objects.get(pk=id)
        message_recu.delete()
        return DeleteMessageRecu(success=True)
# ______________________
# Brouillon

class BrouillonInput(graphene.InputObjectType):
    utilisateur_id = graphene.ID()

class CreateBrouillon(graphene.Mutation):
    brouillon = graphene.Field(BrouillonType)

    class Arguments:
        input = BrouillonInput(required=True)

    def mutate(self, info, input):
        brouillon = Brouillon(**input)
        brouillon.save()
        return CreateBrouillon(brouillon=brouillon)

class UpdateBrouillon(graphene.Mutation):
    brouillon = graphene.Field(BrouillonType)

    class Arguments:
        id = graphene.ID(required=True)
        input = BrouillonInput(required=True)

    def mutate(self, info, id, input):
        brouillon = Brouillon.objects.get(pk=id)
        for key, value in input.items():
            setattr(brouillon, key, value)
        brouillon.save()
        return UpdateBrouillon(brouillon=brouillon)

class DeleteBrouillon(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        brouillon = Brouillon.objects.get(pk=id)
        brouillon.delete()
        return DeleteBrouillon(success=True)
# ______________________
# Corbeille

class CorbeilleInput(graphene.InputObjectType):
    utilisateur_id = graphene.ID()
    message_id = graphene.ID()

class CreateCorbeille(graphene.Mutation):
    corbeille = graphene.Field(CorbeilleType)

    class Arguments:
        input = CorbeilleInput(required=True)

    def mutate(self, info, input):
        corbeille = Corbeille(**input)
        corbeille.save()
        return CreateCorbeille(corbeille=corbeille)

class UpdateCorbeille(graphene.Mutation):
    corbeille = graphene.Field(CorbeilleType)

    class Arguments:
        id = graphene.ID(required=True)
        input = CorbeilleInput(required=True)

    def mutate(self, info, id, input):
        corbeille = Corbeille.objects.get(pk=id)
        for key, value in input.items():
            setattr(corbeille, key, value)
        corbeille.save()
        return UpdateCorbeille(corbeille=corbeille)

class DeleteCorbeille(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        corbeille = Corbeille.objects.get(pk=id)
        corbeille.delete()
        return DeleteCorbeille(success=True)
# ______________________
# Define similar mutations for other models
class Mutation(graphene.ObjectType):
    create_utilisateur = CreateUtilisateur.Field()
    update_utilisateur = UpdateUtilisateur.Field()
    delete_utilisateur = DeleteUtilisateur.Field()

    create_conversation = CreateConversation.Field()
    update_conversation = UpdateConversation.Field()
    delete_conversation = DeleteConversation.Field()

    create_message = CreateMessage.Field()
    update_message = UpdateMessage.Field()
    delete_message = DeleteMessage.Field()

    create_piece_jointe = CreatePieceJointe.Field()
    update_piece_jointe = UpdatePieceJointe.Field()
    delete_piece_jointe = DeletePieceJointe.Field()

    create_destinataire_message = CreateDestinataireMessage.Field()
    update_destinataire_message = UpdateDestinataireMessage.Field()
    delete_destinataire_message = DeleteDestinataireMessage.Field()

    create_copie_carbone = CreateCopieCarbone.Field()
    update_copie_carbone = UpdateCopieCarbone.Field()
    delete_copie_carbone = DeleteCopieCarbone.Field()

    create_message_envoye = CreateMessageEnvoye.Field()
    update_message_envoye = UpdateMessageEnvoye.Field()
    delete_message_envoye = DeleteMessageEnvoye.Field()

    create_message_recu = CreateMessageRecu.Field()
    update_message_recu = UpdateMessageRecu.Field()
    delete_message_recu = DeleteMessageRecu.Field()

    create_brouillon = CreateBrouillon.Field()
    update_brouillon = UpdateBrouillon.Field()
    delete_brouillon = DeleteBrouillon.Field()

    create_corbeille = CreateCorbeille.Field()
    update_corbeille = UpdateCorbeille.Field()
    delete_corbeille = DeleteCorbeille.Field()

class Query(graphene.ObjectType):
    utilisateurs = graphene.List(UtilisateurType)
    conversations = graphene.List(ConversationType)
    messages = graphene.List(MessageType)
    piece_jointes = graphene.List(PieceJointeType)
    destinataires_messages = graphene.List(DestinataireMessageType)
    copies_carbone = graphene.List(CopieCarboneType)
    messages_envoyes = graphene.List(MessageEnvoyeType)
    messages_recus = graphene.List(MessageRecuType)
    brouillons = graphene.List(BrouillonType)
    corbeille = graphene.List(CorbeilleType)

    def resolve_utilisateurs(self, info):
        return Utilisateur.objects.all()

    def resolve_conversations(self, info):
        return Conversation.objects.all()

    def resolve_messages(self, info):
        return Message.objects.all()

    def resolve_piece_jointes(self, info):
        return PieceJointe.objects.all()

    def resolve_destinataires_messages(self, info):
        return DestinataireMessage.objects.all()

    def resolve_copies_carbone(self, info):
        return CopieCarbone.objects.all()

    def resolve_messages_envoyes(self, info):
        return MessageEnvoye.objects.all()

    def resolve_messages_recus(self, info):
        return MessageRecu.objects.all()

    def resolve_brouillons(self, info):
        return Brouillon.objects.all()

    def resolve_corbeille(self, info):
        return Corbeille.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)
