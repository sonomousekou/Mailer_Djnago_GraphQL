from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

class Conversation(models.Model):
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='conversations_expediteur')
    date_creation = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    sujet = models.TextField(blank=True)
    contenu = models.TextField(blank=True)
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

class PieceJointe(models.Model):
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='piecejointe_expediteur')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    nom_fichier = models.CharField(max_length=255, blank=True)
    type_fichier = models.CharField(max_length=50,blank=True)
    taille = models.IntegerField(blank=True)

class DestinataireMessage(models.Model):
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='destinataire_expediteur')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    destinataire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

class CopieCarbone(models.Model):
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='copieCarbone_expediteur')
    message_envoye = models.ForeignKey(Message, on_delete=models.CASCADE)
    utilisateur_cc = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

class MessageEnvoye(models.Model):
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_envoyes_expediteur')
    destinataire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_envoyes_destinataire')
    sujet = models.CharField(max_length=255)
    corps = models.TextField(blank=True)
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

class MessageRecu(models.Model):
    expediteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_recus_expediteur')
    destinataire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_recus_destinataire')
    sujet = models.CharField(max_length=255)
    corps = models.TextField(blank=True)
    date_reception = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

class Brouillon(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="user_brouillon")
    sujet_du_brouillon = models.CharField(max_length=255)
    corps_du_brouillon = models.TextField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

class Corbeille(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="user_corbeille")
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
