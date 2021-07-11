class AddKerberosToAge < ActiveRecord::Migration[6.0]
  def change
    add_column :kerberos, :age, :integer
  end
end
