fontpath=/usr/share/fonts/truetype/malayalam
fonts="AnjaliOldLipi Dyuthi Kalyani Meera Rachana RaghuMalayalamSans suruma"

default:
		@for font in `echo ${fonts}`; \
	do \
		./generate.pe $${font}/$${font}.sfd; done 

install: */*.ttf
	@for font in `echo ${fonts}`; \
	do \
		install -D -m 0644  $${font}/$${font}.ttf ${fontpath}/$${font}.ttf; done

uninstall:
	@for font in `echo ${fonts}`; \
	do \
		if [ -f ${fontpath}/$${font}.ttf ]; then rm -f ${fontpath}/$${font}.ttf; fi \
	done

	if [ -d ${fontpath} ]; then rmdir ${fontpath}; fi

clean:
	@for font in `echo ${fonts}`; \
	do \
		if [ -f $${font}/$${font}.ttf ]; then rm -f $${font}/$${font}.ttf; fi \
	done

