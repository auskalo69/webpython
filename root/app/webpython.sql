USE webpython;    
CREATE TABLE IF NOT EXISTS producto(    
    producto_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY    
    , denominacion VARCHAR(50)    
    , precio DECIMAL(6,2)    
    , barcode VARCHAR(13)
)ENGINE=InnoDB;
