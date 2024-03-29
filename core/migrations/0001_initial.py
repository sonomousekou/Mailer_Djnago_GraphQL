# Generated by Django 5.0.1 on 2024-01-05 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mot_de_passe', models.CharField(max_length=255)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.TextField(blank=True)),
                ('contenu', models.TextField(blank=True)),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
                ('lu', models.BooleanField(default=False)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.conversation')),
                ('expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='PieceJointe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_fichier', models.CharField(blank=True, max_length=255)),
                ('type_fichier', models.CharField(blank=True, max_length=50)),
                ('taille', models.IntegerField(blank=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.message')),
                ('expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='piecejointe_expediteur', to='core.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='MessageRecu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(max_length=255)),
                ('corps', models.TextField(blank=True)),
                ('date_reception', models.DateTimeField(auto_now_add=True)),
                ('lu', models.BooleanField(default=False)),
                ('destinataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_recus_destinataire', to='core.utilisateur')),
                ('expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_recus_expediteur', to='core.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='MessageEnvoye',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet', models.CharField(max_length=255)),
                ('corps', models.TextField(blank=True)),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
                ('lu', models.BooleanField(default=False)),
                ('destinataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_envoyes_destinataire', to='core.utilisateur')),
                ('expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_envoyes_expediteur', to='core.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='DestinataireMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.message')),
                ('destinataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.utilisateur')),
                ('expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinataire_expediteur', to='core.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Corbeille',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.message')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_corbeille', to='core.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='CopieCarbone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('message_envoye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.message')),
                ('expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='copieCarbone_expediteur', to='core.utilisateur')),
                ('utilisateur_cc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.utilisateur')),
            ],
        ),
        migrations.AddField(
            model_name='conversation',
            name='expediteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations_expediteur', to='core.utilisateur'),
        ),
        migrations.CreateModel(
            name='Brouillon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sujet_du_brouillon', models.CharField(max_length=255)),
                ('corps_du_brouillon', models.TextField(blank=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_brouillon', to='core.utilisateur')),
            ],
        ),
    ]
