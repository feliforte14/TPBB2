
// Select the database to use.
use('base_datos_tp_ingenieria_datos2');

db.getCollection('clientes').deleteMany({});
// Insert a few documents into the sales collection.
db.getCollection('clientes').insertMany([
  { 'id_cliente': 1, 'nombre': 'Josefa', 'tipoCliente': 2, 'contraseña':11 },
  { 'id_cliente': 2, 'nombre': 'Enrique', 'tipoCliente': 1 ,'contraseña': 12},
  { 'id_cliente': 3, 'nombre': 'Samanta', 'tipoCliente': 1 ,'contraseña': 13},
]);

// busqueda de clientes tipo 1
const clienteTipo1 = db.getCollection('clientes').find({
    tipoCliente: 1
  }).count();

// Print a message to the output window.
console.log(`${clienteTipo1} clientes de tipo 1`);

db.getCollection('productos').insertMany([
    { 'id_producto': 1, 'descripcion': 'VASO','categorias':[1,4] },
    { 'id_producto': 2, 'descripcion': 'PELOTA','categorias':[2] },
    { 'id_producto': 3, 'descripcion': 'SOGA','categorias':[2,4] },
    { 'id_producto': 4, 'descripcion': 'REPOSERA','categorias':[3,4] },
  ]);

db.getCollection('categorias').insertMany([
    { 'id_categoria': 1, 'descripcion': 'Cristalería' },
    { 'id_categoria': 2, 'descripcion': 'Deportes' },
    { 'id_categoria': 3, 'descripcion': 'Muebles' },
    { 'id_categoria': 4, 'descripcion': 'Articulos del hogar' }
  ]);