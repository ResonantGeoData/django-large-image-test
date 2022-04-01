data "aws_route53_zone" "this" {
  # This must be created by hand in the AWS console
  name = "django-large-image-test.test"
}

data "heroku_team" "this" {
  name = "kitware"
}

module "django" {
  source  = "girder/django/heroku"
  version = "0.10.0"

  project_slug     = "django-large-image-test"
  route53_zone_id  = data.aws_route53_zone.this.zone_id
  heroku_team_name = data.heroku_team.this.name
  subdomain_name   = "www"
}
