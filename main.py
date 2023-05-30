from fastapi import FastAPI, Body, HTTPException, Request;
from fastapi.responses import HTMLResponse;


app = FastAPI();
app.title = "Create a new FastAPI instance";
app.version = "0.0.1";

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 3,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
];

@app.get('/', tags=['Home'])
def message():
    return movies


@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int):
    # manejaremos los parametros de ruta atravez de un try-Except
    try: 
        return movies[id -1]
    except IndexError:
        return {"ERROR": "Movie  is`t 404 Not Found"}

# trabajando con parametros query, que nos permiten extender nuestras busquedas
#NOTA:cuando no defino la recepcion del parametro FastAPI lo infiere como un tipo Query.
# para recibirlo solo agregamos una barra al final
@app.get('/movies/', tags=['Movies'])
def get_movies_by_category(category: str, year: int):
    # haremos el filtrado por categoria usando un for de una solalinea
    findCategory = [ categoria for categoria in movies if categoria['category'] == category ]
    return findCategory or ["404 Not Found"]
    

# _____________________---------------_____________________

@app.post('/movies', tags=['Movies'])
def create_Movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies.append({
        id: id,
        title: title,
        overview: overview,
        year: year,
        rating: rating,
        category: category
    })
    return movies;

# _____________________---------------_____________________
@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, title: str = Body(), overview:str = Body(), year:int = Body(), rating: float = Body(), category: str = Body()):
	for item in movies:
		if item["id"] == id:
			item['title'] = title
			item['overview'] = overview
			item['year'] = year
			item['rating'] = rating
			item['category'] = category
			return movies



# _____________________---------------_____________________
@app.delete('/movies/{id}', tags=['Movies'])
async def delete_movie(id: int):
    for index, item in enumerate(movies):
        if item["id"] == id:
            del movies[index]
            return {'status': 'deleted movie'}

    raise HTTPException(status_code=404, detail="Movie not found")