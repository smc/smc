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
		install -m 0644 malayalam-fonts.conf /etc/fonts/conf.avail/67-malayalam-fonts.conf
		ln -s /etc/fonts/conf.avail/67-malayalam-fonts.conf /etc/fonts/conf.d

uninstall:
	@for font in `echo ${fonts}`; \
	do \
		if [ -f ${fontpath}/$${font}.ttf ]; then rm -f ${fontpath}/$${font}.ttf; fi \
	done

	if [ -d ${fontpath} ]; then rmdir ${fontpath}; fi

	if [ -f /etc/fonts/conf.d/67-malayalam-fonts.conf ]; then \
	rm /etc/fonts/conf.d/67-malayalam-fonts.conf; fi

	if [ -f /etc/fonts/conf.avail/67-malayalam-fonts.conf ]; then \
	rm /etc/fonts/conf.avail/67-malayalam-fonts.conf; fi

clean:
	@for font in `echo ${fonts}`; \
	do \
		if [ -f $${font}/$${font}.ttf ]; then rm -f $${font}/$${font}.ttf; fi \
	done


