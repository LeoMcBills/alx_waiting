from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
import time
import random
from fastapi import Response, HTTPException, status


class Post(BaseModel):
    title : str
    #id : int
    diagnosis : str
    #treated : bool = True
    #time : int




while True:
    try:
        conn = psycopg2.connect(host = "localhost", database = 'fastapi', user = 'postgres', password = '214374',
        cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was Successful")
        break
    except Exception as error:
        print("Connecting to the Dataabase failed")
        print("Error: "+error)
        time.sleep(2)


allPatients = {}

app = FastAPI()


@app.get("/")
def root():
    return {"Patients": "Hey there, this is McBills Technology @Optimus"}

@app.post("/sick", status_code= status.HTTP_201_CREATED)
def posted(patient: Post):
    cursor.execute("""INSERT INTO patients (title, diagnosis) VALUES (%s, %s) RETURNING * """, (patient.title, patient.diagnosis) )
    new_patient = cursor.fetchone()
    conn.commit()
    return {"Add Patient" : new_patient}

@app.get("/patients")
def all_patients():
    cursor.execute("""SELECT * FROM patients """)
    patients = cursor.fetchall()
    return {"data": patients}


@app.get("/patient/{id}")
def one_patient(id: int):
    cursor.execute(""" SELECT * FROM patients WHERE id = %s """, str(id))
    patient = cursor.fetchone()
    if not patient:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
        detail = f"Patient not found, please check your patient id and try again. Thanks.")
    return {"patient_detail": patient}
        

@app.delete("/delete/{id}")
def delete_record(id: int):
    cursor.execute("""DELETE FROM patients WHERE id = %s RETURNING * """, str(id))
    deleted_record = cursor.fetchone()
    conn.commit()
    if deleted_record == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
        detail = f"Patient's record with id: {id} doesn't exist")
    return Response(status_code = status.HTTP_204_NO_CONTENT)


@app.put("/update/{id}")
def update_record(id: int, patient: Post):
    cursor.execute("""UPDATE patients SET title = %s, diagnosis = %s WHERE id = %s RETURNING * """, 
    (patient.title, patient.diagnosis, str(id)))
    updated_record = cursor.fetchone()
    conn.commit()
    if updated_record == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = f"Patient's records with id: {id} doesn't exist!")
    return {"data": updated_record}