from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, orderDetail):
    # Create a new instance of the orderDetail model with the provided data
    db_orderDetail = models.OrderDetail(
        **orderDetail.dict()
    )
    # Add the newly created orderDetail object to the database session
    db.add(db_orderDetail)
    # Commit the changes to the database
    db.commit()
    # Refresh the orderDetail object to ensure it reflects the current state in the database
    db.refresh(db_orderDetail)
    # Return the newly created orderDetail object
    return db_orderDetail


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, orderDetail_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == orderDetail_id).first()


def update(db: Session, orderDetail_id, orderDetail):
    # Query the database for the specific orderDetail to update
    db_orderDetail = db.query(models.OrderDetail).filter(models.OrderDetail.id == orderDetail_id)
    # Extract the update data from the provided 'orderDetail' object
    update_data = orderDetail.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_orderDetail.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated orderDetail record
    return db_orderDetail.first()


def delete(db: Session, orderDetail_id):
    # Query the database for the specific orderDetail to delete
    db_orderDetail = db.query(models.OrderDetail).filter(models.OrderDetail.id == orderDetail_id)
    # Delete the database record without synchronizing the session
    db_orderDetail.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
