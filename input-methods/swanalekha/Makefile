SCIM_TABLES_DIR=/usr/share/scim/tables
SCIM_ICONS_DIR=/usr/share/scim/icons

SRC_DIR=./src
BIN_DIR=./bin
ICON_DIR=./icons

SCIM_MAKE_TABLE=scim-make-table

compile: compile-Malayalam-phonetic

compile-Malayalam-phonetic: $(BIN_DIR)/Malayalam-phonetic.bin

install: install-Malayalam-phonetic
uninstall: uninstall-Malayalam-phonetic

install-Malayalam-phonetic: compile-Malayalam-phonetic
	cp $(BIN_DIR)/Malayalam-phonetic.bin $(SCIM_TABLES_DIR)
	cp $(ICON_DIR)/Malayalam-phonetic.png $(SCIM_ICONS_DIR)

uninstall-Malayalam-phonetic:
	rm $(SCIM_TABLES_DIR)/Malayalam-phonetic.bin
	rm $(SCIM_ICONS_DIR)/Malayalam-phonetic.png


clean:
	rm -f $(BIN_DIR)/*

$(BIN_DIR)/Malayalam-phonetic.bin: $(SRC_DIR)/Malayalam-phonetic.txt.in
	mkdir -p  $(BIN_DIR)
	sed -e \\'s,@SCIM_ICONDIR@,$(SCIM_ICONS_DIR),g\\' $(SRC_DIR)/Malayalam-phonetic.txt.in > $(BIN_DIR)/Malayalam-phonetic.txt
	$(SCIM_MAKE_TABLE) $(BIN_DIR)/Malayalam-phonetic.txt -b -o $(BIN_DIR)/Malayalam-phonetic.bin
	rm $(BIN_DIR)/Malayalam-phonetic.txt
