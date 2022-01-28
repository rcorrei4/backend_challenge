from core.models import models

def criar_event_launch(event_launch, article, db_article, db):
    if event_launch == "events":
        #Pegar o id dentro do dict article
        event_id = str(article.events[0].id)

        #Caso já exista um objeto launches com o id adiciona o mesmo, se não, cria um objeto
        if db.query(models.Events).filter(models.Events.id == event_id).first() is not None:
            db_event = db.query(models.Events).filter(models.Events.id == event_id).first()
            db_article.events.append(db_event)
        else:
            db_event = models.Events(id=event_id, provider=article.events[0].provider)
            db_article.events.append(db_event)

        #Adiciona no banco de dados
        db.add(db_event)
        
    if event_launch == "launches":
        #Pegar o id dentro do dict article
        launch_id = str(article.launches[0].id)

        #Caso já exista um objeto launches com o id adiciona o mesmo, se não, cria um objeto
        if db.query(models.Launches).filter(models.Launches.id == launch_id).first() is not None:
            db_launches = db.query(models.Launches).filter(models.Launches.id == launch_id).first()
            db_article.launches.append(db_launches)
        else:
            db_launches = models.Launches(id=launch_id, provider=article.launches[0].provider)
            db_article.launches.append(db_launches)

        #Adiciona no banco de dados
        db.add(db_launches)

    db.commit()
    return db_article