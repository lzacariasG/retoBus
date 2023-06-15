CREATE OR REPLACE FUNCTION public.cargaregistros(character varying, character varying)
 RETURNS integer
 LANGUAGE plpgsql
AS $function$
DECLARE
	argN ALIAS FOR $1;
	argF ALIAS FOR $2;

	_idArch int4 := 0;
BEGIN 
	SELECT max(f.id) into _idArch
	FROM archivosCargados f WHERE f.nombre = argN AND f.fchcarga = to_date(argF, 'yyyy-mm-dd');
	
	
	INSERT INTO adeudocliente (idcliente, fchcompra , idciudad, empresa, valoradeudo, idarchivo)
	SELECT cl.id, to_date( aa.fch_compra, 'yyyy-mm-dd'), c.id, aa.empresa, aa.valoradeudo::float, _idArch
	FROM archivotmp aa 
	INNER JOIN ciudades c on aa.ciudad = c.ciudad
	INNER JOIN cliente cl on aa.contrato  = cl.contrato and aa.cliente = cl.nombre 
	WHERE aa.idarchivo = _idArch
	ON conflict (idcliente) do nothing ;
	
	UPDATE archivosCargados
	SET
		montoTotal = (SELECT sum (aa.valoradeudo::float)
						FROM archivotmp aa 
						INNER JOIN ciudades c on aa.ciudad = c.ciudad
						INNER JOIN cliente cl on aa.contrato  = cl.contrato and aa.cliente = cl.nombre 
						WHERE aa.idarchivo = _idArch),
		registrosCargados = (SELECT COUNT (aa.valoradeudo::float)
						FROM archivotmp aa 
						INNER JOIN ciudades c on aa.ciudad = c.ciudad
						INNER JOIN cliente cl on aa.contrato  = cl.contrato and aa.cliente = cl.nombre 
						WHERE aa.idarchivo = _idArch)
	WHERE id = _idArch;

	UPDATE archivosCargados
	SET
		registroserror = (SELECT COUNT(*) FROM archivotmp aa WHERE aa.idarchivo = _idArch) - registroscargados
	WHERE id = _idArch;


	RETURN _idArch;
END;
$function$
;
