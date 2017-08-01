CREATE TABLE "userprofile" (
	"user_id" serial NOT NULL UNIQUE,
	"user_name" varchar(45) NOT NULL UNIQUE,
	"user_email" varchar(45) NOT NULL UNIQUE,
	"user_pass" varchar(45) NOT NULL UNIQUE,
	CONSTRAINT userprofile_pk PRIMARY KEY ("user_id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "product" (
	"product_id" int NOT NULL UNIQUE,
	"product_name" varchar(45) NOT NULL UNIQUE,
	CONSTRAINT product_pk PRIMARY KEY ("product_id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "feedback" (
	"feedback_id" serial NOT NULL UNIQUE,
	"name" varchar(45),
	"email" varchar(45),
	"product_id" int NOT NULL,
	"rating" int NOT NULL,
	"comment" varchar(250),
	"feedback_time" DATE NOT NULL,
	CONSTRAINT feedback_pk PRIMARY KEY ("feedback_id")
) WITH (
  OIDS=FALSE
);

ALTER TABLE "feedback" ADD CONSTRAINT "feedback_fk0" FOREIGN KEY ("product_id") REFERENCES "product"("product_id");

