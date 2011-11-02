# getFiles ( files , extension )

Get a list of files from a list that use the extension.

## Parameters

### files

 array of file paths, generally received from the argv

### extension

 extension of files you want. Does not contain the preceding period.
If you want all .py files, send "py" as your extension.
	

## Returns
### default

list of files that are indeed the right extension.
	
-----

# getFiles ( files , extension , excludeFile )

Get a list of files from a list that use the extension, but don't include a
certain file.

## Parameters

### files

 array of file paths, generally received from the argv

### extension

 extension of files you want. Does not contain the preceding period.
If you want all .py files, send "py" as your extension.

### excludeFile

 the full name of the file you want to exclude, generally
the name of the file being called if you use `argv` for your files array.
This is useful when your extension is `py`, because you can tell the
script to NOT look at itself. Always useful.
	

## Returns
### default

list of files that are indeed the right extension.
	
-----

# grabDocifyBlock ( file )

Get the docify block, using the default docify block declarations `/**` to start
and `*/` to stop.

## Parameters

### file

 The file you're going to grab the docify blocks from.
	

## Returns
### default

A list of parsed docify blocks.
	
-----

# grabDocifyBlock ( file , start , stop )

Get the docify block, using custom start and stop declarations.

## Parameters

### file

 The file you're going to grab the docify blocks from.

### start

 The pattern for the start of a docify block.

### stop

 The patter for the end of a docify block.
	

## Returns
### default

A list of parsed docify blocks.
	
